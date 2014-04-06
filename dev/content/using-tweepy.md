Title: Best Practices for Querying Twitter API using (forked) tweepy
Date: 2013-04-28 17:33
Author: grinbergnir
Category: Uncategorized
Slug: using-tweepy
Picture: images/twython1.jpg

Over the past few weeks I have been accessing Twitter API from python
using tweepy. In the course of doing so, I added support in tweepy for
using multiple authentication handlers, monitoring rate limits, waiting
when running out of calls, support for search using Twitter API v1.1,
proper pagination of results and more. In this blog post I will describe
the major changes in my forked version of the tweepy package and provide
some best practices and examples for querying the Twitter API robustly.
Fork me on [GitHub](http://github.com/nirg/tweepy) or follow my pull request on the main tweepy repo
[\#282](http://github.com/tweepy/tweepy/pull/282) to get the complete code referenced in this post.

New Features
------------

-   **Support for multiple authentication handlers**: sometimes you just
    need more than a single authentication handler. You can provide a
    list of authentication handlers to tweepy and manually switch
    between them:  
        
        :::python title="using multiple authentication handlers"
        import tweepy

        # create authentication handlers given pre-existing keys  
        auths = []  
        for consumer_key, consumer_secret, access_key, access_secret in oauth_keys:  
            auth = tweepy.OAuthHandler(consumer_key, consumer_secret)  
            auth.set_access_token(access_key, access_secret)  
            auths.append(auth)

        api = tweepy.API(auths)

        # switch to the second authentication handler (zero-based index)  
        api.auth_idx = 1  

-   **Monitoring rate limit**: switching authentication handlers
    manually is nice, but it is far more useful to have tweepy do that
    automatically based on the number of remaining api calls.
    The `monitor_rate_limit` argument does exactly that - monitor to
    number of remaining calls to the Twitter API endpoint and switch to
    the next authentication handler when running out of calls. This
    feature lets you be a good citizen and not supersede your API calls
    quota.  

        :::python
        api = tweepy.API(auths, monitor_rate_limit=True)

-   **Blocking when running out of calls**: using the argument
    wait\_on\_rate\_limit you can have tweepy wait when running out of
    calls. By monitoring the http headers returned from Twitter, tweepy
    now knows exactly how long to wait until the next lump of api calls
    is available. This is useful when you need more than the number of
    calls allowed by the rate limit, but don't want your program to fail
    with an exception or lose track of the current position in your
    results.  

        :::python
        api = tweepy.API(auths,
                    monitor_rate_limit=True, wait_on_rate_limit=True)

-   **Proper iteration of result pages (pagination)**: prior to my
    forked version of tweepy, if you used the Cursor object to iterate
    over results you probably have missed some tweets in your result
    set. A good explanation of why this has happened is in Twitter own
    documentation on [working with timelines](https://dev.twitter.com/docs/working-with-timelines). Now iteration uses
     `max_id` parameter to properly traverse results when using the
    cursor object. If you're wondering what's happening behind the
    scenes, take a look at `MaxIdIterator` class in `tweepy/cursor.py`.
-   **Search endpoint now supports Twitter API v1.1**.
-   **Unit testing for all of the above**.

Best Practices
--------------

-   **Retrying on errors**: little know fact, unless you don't dig into
    the tweepy code, is that you can have tweepy retry making calls for
    you when certain error codes are returned. The retry feature is
    useful for handling temporary failures. You specify how many retries
    will be performed, delay in seconds between calls and the error
    response codes upon which tweepy will retry making calls. For a
    complete list of error response codes, see the Twitter API
    documentation on [Error Codes & Responses](https://dev.twitter.com/docs/error-codes-responses "Error Codes & Responses"). Here is an example of
    using the retry feature:  

        :::python
        api = tweepy.API(auths, retry_count=3, retry_delay=5,
                         retry_errors=set([401, 404, 500, 503]))

-   **How to use pagination with search?** here is the example from
    `examples/paginated_search.py`:  

        :::python title="example of iterating over paginated search results"]  
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)  
        auth.set_access_token(access_token, access_token_secret)

        api = tweepy.API([auth], 
                # support for multiple authentication handlers  
                # retry 3 times with 5 seconds delay when getting these error codes
                # For more details see 
                # https://dev.twitter.com/docs/error-codes-responses  
                retry_count=3,retry_delay=5,retry_errors=set([401, 404, 500, 503]), 
                # monitor remaining calls and block until replenished  
                monitor_rate_limit=True, wait_on_rate_limit=True 
        )

        query = 'cupcake OR donut'  
        page_count = 0  
        for tweets in tweepy.Cursor(api.search, q=query, count=100,
                        result_type="recent", include_entities=True).pages():  
        page_count += 1  
        # print just the first tweet out of every page of 100 tweets  
        print tweets[0].text.encode('utf-8')  
        # stop after retrieving 200 pages  
        if page_count >= 200:  
            break  

-   **Response as python dictionary**: sometimes you don't want tweepy
    to spend time on parsing json into dedicated python object and have
    the results simply as a dictionary. The example at
    `examples/json_results.py` demonstrate querying a user timeline, tim
    oreilly in this case, using a json payload type:  

        :::python title="example of changing payload type"]  
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)  
        auth.set_access_token(access_token, access_token_secret)

        api = tweepy.API([auth])  
        json_user_timeline = tweepy.binder.bind_api(  
            path = '/statuses/user_timeline.json',  
            payload_type = 'json', payload_list = True,  
            allowed_param = ['id', 'user_id', 'screen_name', 'since_id',
                             'max_id', 'count', 'page', 'include_rts'])

        # iterate over 50 of tim oreilly's tweets  
        for tweet in tweepy.Cursor(json_user_timeline, api,
        screen_name='timoreilly', count=20, include_rts=True).items(50):  
        print tweet['text'].encode('utf-8')  
        
Have a comment? an idea of how to do things more elegantly? leave a comment or contact me on twitter @grinbergnir.