Title: WSDM 2014 Summary, Opinions and Other Thoughts
Date: 2014-02-28 08:21
Author: grinbergnir
Category: Uncategorized
Slug: wsdm-2014-summary-opinions-and-other-thoughts
Picture: images/WSDM2014-text-logo.png

It was a great attending WSDM this year, right at the heart of NYC! I could not possibly cover all that went down there in the three days of the conference, but would use this post to highlight sessions and talks that I attended and found particularly interesting.

The conference itself was a single track mixture of mostly long, 20 minutes talks and few shorter talks. The sessions revolved around Web Search, Advertising, Recommender Systems, Network Analysis, Language Analysis and Crowdsourcing.

The **Web Search** Session was very good with several papers that took new and interesting perspectives to the “old" problem of search. In [[1]](#ref1) Demeester et al. modeled disagreement between user rankings of top results and used it to improve ranking of search results. Another novel perspective was introduced by Hassan et al. in [[2]](#ref2), which learned to distinguish between long search sessions where the user is satisfied or struggling and unsatisfied. Li et al. looked in [[3]](#ref3) at the phenomena of click spam: when spammer try to game search engines by automatically generating clicks on preferable results.

Personally, I found the **Advertising** sessions somewhat disappointing due to their (usual) focus on complex models that result marginal performance improvements, which rarely teach us something about users, ads or the search process. I get it -  someone has to pay the bills and minor improvements in modeling ads may lead to huge improvements in revenue. Nevertheless, I would much rather see models that actually teach us something about the process than just building a bigger, stronger hammer.

The **Log Analysis** session was GREAT! I highly recommend looking at all papers, but just to pick a few: the best paper winner [[4]](#ref4) by Lagun et al. identified common motifs in mouse movement over search results; [[5]](#ref5) by Wang et al. learned jointly the user assignment to clusters and their resulting clicking behavior; [[6]](#ref6) by Scaria et al. devised a game where participants have to get from a source wikipedia entry to a target entry by only following links and studied differences between successful and unsuccessful sessions.

The **NLP**and **Topic Modeling** sessions were pretty much standard LDA papers: we devised this graphical model, inferred it using Gibbs sampling and evaluated it by using perplexity on held-out. Two exception to that, can be found in [[7]](#ref7) and [[8]](#ref8). Yu et al. used topics models in [[7]](#ref7) to diversify E-commerce search results and evaluated its success in user satisfaction. Bi et al. found topic-specific experts in [[8]](#ref8) and verified their results using external dataset.

From the **Peer Production; Data Analysis** session two papers stood out. First, the work by Abisheva et al. in [[9]](#ref9) included a thorough analysis of the cross-section between YouTube and Twitter with interesting takes on the demographics of the platforms and identification of promotional account. Second, the paper by Di et al. in [[10]](#ref10) looked at how image features such as the number images or their quality effect purchasing consumer decisions at eBay.

Have any questions or comments? leave a comment below or contact me @grinbergnir.

### References:

<a name="ref1"></a>[1] [Exploiting user disagreement for search evaluation: an experimental approach](http://wwwhome.ewi.utwente.nl/~hiemstra/papers/wsdm2014.pdf), Thomas Demeester, Robin Aly, Djoerd Hiemstra, Dong Nguyen, Dolf Trieschnigg, Chris Develder <br/>
<a name="ref2"></a>[2] [Struggling or Exploring? Disambiguating Search Sessions](http://research.microsoft.com/en-us/um/people/ryenw/papers/HassanWSDM2014.pdf), Ahmed Hassan, Ryen W. White, Susan T. Dumais, and Yi-Min Wang <br/>
<a name="ref3"></a>[3] [Search Engine Click Spam Detection Based on Bipartite Graph Propagation](http://www.thuir.cn/group/~YQLiu/publications/wsdm2014.pdf), Xin Li, Min Zhang, Yiqun Liu, Shaoping Ma, Yijiang Jin, Liyun Ru <br/>
<a name="ref4"></a>[4] [Discovering Common Motifs in Cursor Movement Data for Improving Web Search Ranking](http://www.mathcs.emory.edu/~dlagun/pubs/motifs_wsdm2014.pdf), Dmitry Lagun, Mikhail Ageev, Qi Guo, Eugene Agichtein <br/>
<a name="ref5"></a>[5] [User Modeling in Search Logs via A Nonparametric Bayesian Approach](http://sifaka.cs.uiuc.edu/~wang296/paper/wsdm488.pdf), Hongning Wang, ChengXiang Zhai, Feng Liang, Anlei Dong, Yi Chang <br/>
<a name="ref6"></a>[6] [The Last Click: Why Users Give up Information Network Navigation](http://cs.stanford.edu/people/jure/pubs/navigation-wsdm14.pdf), Aju Thalappillil Scaria, Rose Marie Philip, Robert West, Jure Leskovec <br/>
<a name="ref7"></a>[7] [Latent Dirichlet Allocation based Diversified Retrieval for E-commerce Search](http://web.engr.oregonstate.edu/~wong/papers/pdf/WSDM2014.pdf), Jun Yu, Sunil Mohan, Duangmanee Putthividhya, Weng-Keen Wong <br/>
<a name="ref8"></a>[8] [Scalable Topic-Specific Influence Analysis on Microblogs](http://oak.cs.ucla.edu/~cho/papers/wsdm2014.pdf), Bin Bi, Yuanyuan Tian, Yannis Sismanis, Andrey Balmin, Junghoo Cho <br/>
<a name="ref9"></a>[9] [Who Watches (and Shares) What on YouTube? And When? – Using Twitter to Understand YouTube Viewership](http://ingmarweber.de/wp-content/uploads/2014/02/Who-Watches-and-Shares-What-on-YouTube-And-When-Using-Twitter-to-Understand-YouTube-Viewership.pdf), Adiya Abisheva, Venkata R. Kiran Garimella, David Garcia, Ingmar Weber <br/>
<a name="ref10"></a>[10] [Is a picture really worth a thousand words? – on the role of images in e-commerce](http://labs.ebay.com/events/event/news-vision-paper-accepted-at-wsdm-2014), Wei Di, Neel Sundaresan, Robinson Piramuthu, Anurag Bhardwaj <br/>