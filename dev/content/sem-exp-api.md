Title: Our Semantic Keyword Expansion API is ON!
Date: 2013-05-19 16:36
Author: grinbergnir
Category: Uncategorized
Slug: sem-exp-api
Picture: images/zoom_into_pmi_topic1.png

If you ever wanted to track a certain topic on Twitter, you probably wondered what keywords people are using to refer to it. Our new Semantic Expansion API lets you do exactly that - given a short list of keywords, it finds keywords that appear in a similar context or directly with the initial list. How is this useful? by tracking more keywords you get a more robust and complete coverage of desired topics. What is "semantic" about it? using co-occurrence patterns from individual tweets lets us preserve the semantic structure already embedded in tweets and capitalize on it for keyword expansion. In this blog post I'll briefly describe our expansion methods, the methods' API and provide examples for using it from Python.

Expansion Methods
-----------------

Two of the coolest outcomes of our work "*Extracting Diurnal Patterns of Real World Activity from Social Media*" are methods for semantically expanding a list of keywords using Twitter co-occurrence patterns. Raw co-occurrence counts of words can be noisy sometimes and so our methods use the more stable [Pointwise Mutual Information (PMI)](http://en.wikipedia.org/wiki/Pointwise_mutual_information). Our methods traverse the PMI graph (image above) in several ways and select keywords for inclusion.

The Aggregated PMI (APMI) method consider terms appearing directly withthe initial set of keywords. For example, when starting from the hashtag"\#aurora" (as in the PMI graph above), APMI may consider including"shooting", "colorado" and "theater" in the expanded list. Our secondexpansion method, ContextPMI, examines the context of initial seed listand find keywords that have similar context. Following on the previousexample, ContextPMI would look for keywords with "shooting", "colorado"and "theater" in their context.

The actual methods are more involved than described here: we need tohandle common and corpus-specific stopwords and exclude words relevantonly to a small subset of the initial seed list. The interested readershould refer to the <a href="/papers/grinberg-icwsm2013-extracting.pdf" target="_blank">full paper<img src="/images/pdf-icon-16x16.png"></a> for more details.

Semantic Expansion API
----------------------

Our Semantic Expansion API provide two endpoints: AGG\_PMI and CONTEXT\_PMI, which are shortens for the Aggregated PMI and Context PMImethods described earlier. Both methods are accessible through HTTP GET requests, taking a list of keywords for expansion as input and return an expanded list of terms with their scores. The two endpoints support few other parameters:

##### AGG\_PMI Endpoint

* terms (required): comma-separated list of keywords for expansion as string (url encoded).
* top\_n: number of top terms to return, according to their score. Defaults to 100.

##### CONTEXT\_PMI Endpoint

* terms (required): comma-separated list of keywords for expansion as string (url encoded).
* freq\_cutoff: minimum document frequency of returned terms over a period of two months. Defaults to 200 and values below that will be ignored.
* bootstrap\_samples: integer, number of times to bootstrap the seed list in building the context for the method. Defaults to 100.
* score\_cutoff: integer, specifying the minimum score for returned terms. Defaults to 500.

Both methods return a list of terms and their corresponding scores as a json object.

Using the API from Python
-------------------------

As a Python enthusiast, it was natural for me to write a service client in python. The *semexpweb.py* module has *Client* class, which provide a convenient, pythonic way for querying the API. To instantiate a Client object do the following:

    :::python Instantiating an API Client
    import semexpweb  
    c = semexpweb.Client(server='Contact me for server info')  

You can also specify a timeout for the HTTP request (defaults to 60). The IP above points to our server and should rarely change.

Once you have the client object you can give it a list of keywords for expansion, in this example a list of coffee related terms:

    :::python Example of Keyword Expansion using ContextPMI firstline="3" wraplines="true"
    coffee_terms = ['coffee', '#coffee', 'starbucks', '#starbucks', \\  
                    'espresso', '\#espresso', 'lovecoffee', '#lovecoffee', \\  
                    'caffeineaddict', '\#caffeineaddict', 'venti', '#venti', \\  
                    'starbucks', '#starbucks', 'mugs', '#mugs', 'latte', \\  
                    '#latte', 'caf', '#caf', 'coffeebean', '#coffeebean']  
    print c.context_pmi(coffee_terms)  

The output should look like this:  

    :::python
    [[u'#mocha', 2656], [u'#barista', 2570], [u'#cappuccino', 2565], 
     [u'#starbuck', 2231], [u'#caramel', 2183], [u'#frappuccino', 2103], 
     [u'#iced', 1892], [u'#latteart', 1860], [u'macchiatos', 1776], 
     [u'macchiato', 1769], [u'frappucino', 1738], ... ]

Source Code
-----------

The source code for using the API as described in this post is in <a href="/files/SemExpWeb.zip" target="_blank">SemExpWeb.zip<img src="/images/zip-icon-16x16.png"></a>. You would find in the archive both the *semexpweb.py* module and *usage\_example.py* containing the example code in this post.

Have any questions or comments? leave a comment down below or contact me @grinbergnir.
