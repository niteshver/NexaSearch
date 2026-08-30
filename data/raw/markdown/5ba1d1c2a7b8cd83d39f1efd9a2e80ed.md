# Notes on Habbema *et al.* (2015):
                            "Realizing a Desired Family"

                        Posted on Oct 24, 2021

This article is both a personal essay and a rough note.

**Personal essay:** This essay covers a sensitive, personal topic. If you chose to read it, I'd be grateful if
                                you could be extra charitable in interpreting it.

**Rough note:** Writing rough notes allows me share more content, since polishing takes lots of time.
                                While I hope it's useful, it's likely lower quality and less carefully considered than my
                                usual articles.
                                It's very possible I wouldn't stand by this content if I thought about it more.

Recently, I’ve been trying to understand the literature on age and fertility. I really want to have children, and the thought of not being able to have biological children is honestly kind of scary to me. As I've started to get closer to turning 30, it's felt important to try to develop an accurate picture: how do one's chances of successfully having a family change as they get older?

When I express these worries to friends, I often get the response that men don't need to worry about age and fertility. It seems to me that this is mistaken. It is true that, as a male, my future partner’s age will likely have a much larger direct effect than mine. But the same trend still has a profound indirect effect on me: to the extent my partner's age is correlated with mine, my opportunity to have kids will be affected in the same way. As a result, when I see curves showing the relationship between "maternal age" and various measures of fertility, I think projecting my own age on to the graph is probably a reasonable rough first order way to think about the consequences for me. (To improve on this, one could convolve with a distribution modelling partner age gaps.) Of course, an indirect effect is probably less scary than a direct one, and I don't mean by any of this to imply anything about the relative merit of my worry to anyone else's.

In general, this is a sensitive topic. If you're reading this essay, there's a decent chance it's a really important and sensitive topic to you. It's also a sensitive and deeply important topic for me. These are my personal, rough notes. I'd be really grateful if you could be charitable in reading them.

## Probability of achieving a “desired family size”

In trying to understand fertility and age, many resources I found just weren’t that helpful. Most resources give raw probabilities for conception per month at a given maternal age. But turning those raw statistics into a good estimate of the complete probability a couple will successfully have a child, let alone several, is actually tricker than it first appears. Not only is the probability of conception across months not independent, but it can change surprisingly rapidly.

From this perspective, Habbema *et al.*
                                2015 is a
                            remarkably useful paper. They build a model to estimate the probability a couple, for a
                            given initial maternal age, will be able to achieve a given “desired family size.”
                            (They focus on maternal age because it typically has a much larger effect, but note that if the male partner is "much
                            older" this assumption breaks down.)
                            I’m
                            not qualified to evaluate the medical aspects, but their paper does a great job of
                            picking a question that’s relevant to people who want to have kids.

The main result of Habbema is this table, showing the maternal age you need to start start trying at, if you want to achieve a family of a given size with a given probability:

Although that table is interesting, it isn’t *really* the question I want to ask. In
                            principle, their data (if you trust it) allows one to ask a much broader range of questions.
                            Unfortunately, their paper doesn’t do any of the analyses I think would be most interesting!
                        

So, I tried to extract the data from their graphs and do the analyses I wanted myself. I did this by hand, so the data might be off by a percentage point here or there, but I think I got things pretty accurate. (You can download a csv of my approximate version of their data if you want to analyze it!)

My main takeaways are:

- The number of children you want has a big effect: at some points, the difference between wanting 3 children and 1 can be equivalent to as much as a 12 year age difference. (More typically, it's a 5-7 year difference.)
- Starting a single year earlier can matter a shocking amount: there are points where your likelihood of achieving a desired family size drops 10%/year.
- IVF matters less than I would have hoped. By the mid 30s, it’s equivalent to a 1-3 year difference. (It’s important to be clear that their IVF scenario does not include egg freezing at a younger age.)

The following analysis is very rough, and a quick side project I did, on a topic far outside my area of expertise. I thought I might share it in case it's useful to others, but please take it with a big grain of salt!

## Lack of Egg Freezing Data

Before going on, it's worth emphasizing a huge limitation with Habbema data: it doesn't include a model for egg freezing. Egg freezing is an increasingly common option (especially among people I know), and it seems like a pretty drastic improvement over basic IVF. Unfortunately, since all the analysis below relies on Habbema's data, I'm unable to account for the affects of egg freezing.

If you are pursuing egg freezing, I'd guess most of the following analysis isn't very relevant and is overly pessimstic, especially if you froze them at a younger age. There's a lot of nuances that actually make it tricky to extrapolate a model like the Habbema one, and I'm definitely not an expert, so I'm actually quite uncertain what things would look like for you except "probably quite a bit better."

With that said, despite egg freezing's increasing prominence, I think the Habbema data is still very relevant. It's still very uncommon overall. And as a male, I see the non-egg freezing case as very relevant to me, since I don't know if my future partner will have frozen their eggs.

I'll try to reiterate the egg freezing limitation throughout this essay so that it's visible to someone skimming.

## Data overview

Fundamentally, the data we get from Habbema *et al.* is the probability
                            that
                            a couple will achieve a desired family size for a given maternal starting age,
                            depending on whether they'd like one, two, or three children, and whether they are able and
                            willing to resort to IVF.
                            (In the IVF case, it's assumed the couple starts trying to conceive naturally, and
                            transitions to IVF when a fertility specialist following standard practices recommends it.)
                            Unfortunately, egg freezing is not considered.
                        

Habbema *et al.* then use this to determine the latest
                            age one can start trying
                            and
                            have a given probability of achieving a given family size.
                            They give these ages for 90%, 75%, and 50% probability.
                            I wanted something more comprehensive, so I made the following visualization:

## What’s the cost of waiting a year?

I suspect for many people, the most powerful tool to give them is an understanding of the marginal cost of waiting a year.

One useful way to look at this is the lost probability of achieving a desired family size due to waiting an additional year. I’ve also included a plot showing the lost fraction of one’s remaining probability of reaching a desired family size: although the absolute probability change is helpful for thinking about expected value, if one’s committed to trying to have children and it’s a question of when, the fraction of remaining probability plot determines how much worse one option is than another.

I was really surprised just how sharp these peaks are. It feels like waiting a single year can’t possibly matter that much, so I was quite surprised that there are points where waiting a single year can cost 10% of one’s probability of achieving a desired family size, or as much as 30% of one’s remaining probability. (But keep in mind that egg freezing would probably improve things quite a bit.)

Another useful way to look at this is to ask how many years of waiting, at a given age, are equivalent to accepting a given “risk budget”. We see that accepting a 10% increase in the risk of not achieving a desired family size is worth 10+ years at 20, but almost linearly falls from there:

Of course, there are many other, additional costs to waiting an additional year, which aren’t captured by the probability delta. For example, going through a miscarriage seems like an emotionally painful experience for a couple, beyond it’s effect on this probability. The difficulties of a pregnancy might also be increased. On the other hand, there are many countervailing costs one would need to weigh all of this against.

## How much does the number of kids you want matter?

One thing that really stands out to me in the above plots is just how much the desired family size matters. To understand this better, I looked at the difference in probability between achieving a family size of 1 and N as a function of age. (For simplicity, I focused on the non IVF case.)

An alternative way to look at this is to try to convert the difference between different family size goals into numbers of years. For each age and scenario, I determined how many years older someone only aiming to have one child and willing/able to use IVF could be and have the same probability.

This plot is a bit weird. It’s technically true (according to Habbema’s data) that a woman aiming to have 3 kids without IVF starting at the age 20 has the same probability as a woman 16 years older only aiming to have one child with IVF. But that’s mostly because the year to year changes in probability in the 20s are very small.

I think the more useful, functional frame is probably something like “If you are planning to have children in your 30s and you want to have three children, it might be useful to think of yourself as effectively being 5-7 years older than someone who wants one. If you want two children, it might be useful to think of yourself as 3-4 years older than someone who only wants one.”

## How much does IVF help?

Something else that surprised me about the Habbema data is how little IVF seems to help:

To be clear, in a lot of cases IVF means you can start having kids 2-5 years later with the same probability of achieving desired family size, and that’s a big win. But I honestly expected more. Habbema and colleagues try to defend IVF on this point: “The impact of IVF on starting age should not be confused with the effectiveness of IVF in terms of an increase in chance of success. The increase in the chance of realizing a two-child family by using IVF is considerable (6–8%) for starting ages between 30 and 40...” But I would have expected more than 6-8%.

                            As mentioned earlier,
                            it’s important to be clear that their IVF scenario does not include egg freezing. I think
                            freezing eggs at a younger age and then having children later is increasingly becoming
                            popular,
                            and my interpretation is that the IVF numbers are not informative about one's
                            chances
                            if they do that. I haven’t looked into this super carefully, but if you’re trying to get a
                            better
                            model of this, Pelin *et
                                    al.*
                                (2014) and
                            Mesen *et al.*
                                (2016)
                            seem
                            useful. Unfortunately, I can’t find any papers jointly modelling the probability of live
                            births given the age of oocyte retrieval and the age when a patient tries to get
                            pregnant. I’m moderately worried that a lot of resources may be misleading in only
                            focusing on probability conditioned on the retrieval age, when Pelin *et al.* find that
                            age
                            at attempted pregnancy affects success probability by 2-3x, and it’s very easy to
                            imagine correlations between the age of freezing and the age of attempted pregnancy.
                            Despite this, the evidence seems really strong that egg freezing helps a lot over IVF.
                            

                                I'd be really excited for someone to
                            do a careful model like Habbema *et al.* which includes egg freezing.
                            I'd be especially interested in understanding how egg freezing affects the probabilities for having multiple
                            children in people, especially in people who don't freeze especially early.
                            I suspect there are a large number of people who begin thinking about fertility at an age where it's quite likely
                            they can have one child, but multiple may be tricky. If egg freezing can "lock-in" the probability of having one
                            child and extend it to, say, be the probability of having three children that would seem very impactful.
                        

## Interesting Quotes from Habbema’s Discussion

- “From fertility-awareness studies and population surveys, we know that most young people are too optimistic about their chances to conceive spontaneously after age 35”
- “[Y]oung people tend to overestimate the effectiveness of IVF”
- “Couples who are highly motivated to conceive and are well informed of the best period within a cycle to conceive can sometimes reach higher fecundabilities than the 0.23 used in the baseline”
- “The results on latest starting age assume that the couples start trying for the next pregnancy 15 months after the birth of a child…. For example, for a period of 9 instead of 15 months, the latest starting age will be half a year later for a two-child family, and one year later for a three-child family.”
- “[These] calculations are based on population data, and therefore apply to couples for which age is the only known fertility-related attribute. This is usually the case when couples start building a family, but not after a fertility investigation has been performed. A more informed prognosis of natural conception is now possible, by taking the results of the fertility investigation into account.”

## What if you haven't yet found a partner to have children with?

The analysis above still doesn't quite get at the heart of the matter for me. I'm single: I don't have a serious option to have a family right now. It will probably be several years before I find the right person to have a family with. This means that my present age isn't the right thing to consider.

This section will attempt to model in the process of finding a partner. To do this, we're going to have to make a lot of dubious modelling assumptions, so please take this with even more salt than you have the rest of these notes!

In my previous essay on micromarriages, I estimated that people in the United States between the ages of 18 and 35 have a 5% chance of meeting the person they marry per year, extrapolating from population level statistics about marriage. Since 60% of children are born to married couples, we'll estimate that the probability of meeting the person one has children with is 8.3%/year (5%/0.6).

So we might expect that if someone is single (or with a partner they won't have kids with) and wants kids, there's a 8.3% chance they meet the person they'll eventually have children with that year, a (100%-8.3%) * 8.3% the next year, and so on. Of course, it seems like having a child the year one meets is unusual, so we should also account for some amount of "wait period" -- perhaps 2 years if timelines are tight. This gives us a distribution over ages one might start trying to have children at, which can then be used to integrate over the Habbema data.

That gives us the following:

This is a dubious model, based on dubious assumptions. For example, we extrapolate from global population statistics about marriage and people having children, but many people may not be looking to marry or have children. As a result, people who are actively looking for these things likely have higher probabilities. Additionally, readers of this article may tend to be highly educated, and may tend to meet the person they have children with at a later age. And even if it was accurate would have lots of caveats. For example, it doesn't account for egg freezing. Despite all this, I think having a bad model is often better than having no model (as long as you know the model is bad).

My initial reaction to this graph is to find it quite disheartening. But the good news is that these even if these numbers are true in some aggregate sense, they're more under our control than the models that were purely about fertility. The probability one meets their partner in the next year doesn't have to be the 8.3% average we estimated. (In fact, if you care a lot about finding a partner, it's probably higher already.)

From this perspective, I'm inclined to see the the graph not as telling me an immutable fact, but rather telling me that if this is important to me and I don't like the default probabilities, it's something I need to act on. For myself, I'm (1) trying to be more open about the fact that I'm looking for a partner to have children with (so that compatible partners might be able to find me); (2) asking friends if they know anyone I should meet; and (3) sometimes organizing matchmaking parties to help people in my social circle find partners (and maybe inspire them to help me find someone as well).

**Looking for a partner to (someday) have kids with?**
                            

I'm a monogamous, straight, 29 year old male who really wants to have kids someday. I’d love to meet someone who shares my excitement to have kids, love of math, and interest in effective altruism.

If you think we might be compatible, consider sending me an email or DMing me on Twitter. (I'm single as of updating this essay in September 2022.) If you're on the fence about reaching out, you might find my "date me" doc and my essay on micromarriages interesting.