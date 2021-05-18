## Solution Architect FAQ

#### - Blaise Pabon

---

## Question 1:
> Hello,
I'm new to search engines, and there are a lot of concepts I'm not educated on. To make my onboarding smoother, it'd help if you could provide me with some definitions of the following concepts:
> - Records
> - Indexing

George, yes, it's common for anyone new to search to feel a bit overwhelmed.
We make an ongoing effort to arrange the concepts in a coherent sequence.
It turns out that you are right on schedule because _Records_ and _Indexing_ are the topics that come up at this point in the process.

####Records

An Algolia record (or object) is a set of key-value pairs called attributes. Attributes are similar to fields, yet they don’t have to respect a schema and can change from one object to another.
You can also think of the attributes as facts which describe the same piece of data, so you will want to include any information that facilitates
	- search,
    - display on the front end,
	- filtering,
	- or relevance.
Algolia uses the properties of the fields to improve search results.
Algolia can also use the fields to create a sequence of records and provide results more quickly.

####Indexing

[Indexing](https://www.algolia.com/doc/guides/indexing/indexing-overview/#overview) is the process of arranging references to fields so that you can locate their the corresponding records without waiting to read the content.
Indexing is also useful to calculate facts about the collection of records; such as the total, the most/least recent, etc.

>I'm also struggling with understanding what types of metrics would be useful to include in the "Custom Ranking."
>
>Cheers,
>George

In general, you will want to consider custom ranking in any situation where you want to determine the order using a combination of several values.
Let's say that you want to broadly represent sentiment analysis by combining "Likes" and "re-tweets".
At index time, Algolia will create a third index, representing the combination of both metrics.

Thank you for bringing these questions to my attention. It helps me track the effectiveness of our onboarding process and identify where we can improve.

---

##Question 2:
>Hello,
Sorry to give you the kind of feedback that I know you do not want to hear, but I really hate the new dashboard design. Clearing and deleting indexes are now several clicks away. I am needing to use these features while iterating, so this is inconvenient.
Regards,
Matt

Hi Matt, **thank you** for bringing this to my attention, you are providing me with information I can't easily obtain.
Please enjoy the beverage of your choice with the attached gift card.
You will also notice a new badge on your profile for the _power user_ achievement.
Speaking of power usage, I want to confess that the design goal of the dashboard is to provide casual users with access to the features; and to
illustrate the structure of the service.
If your goal is to reduce the number of clicks you need to make to update your config, I can propose two automation strategies to consider
I'm happy to provide you with concrete examples of whichever one you pick:
- On demand: you can trigger the edits/delete steps from a command line or via integration with a web app of your own.
- Batch: you can extend your content management system to trigger the steps as part of some existing workflow.

---

##Question 3:
> Hi,
I'm looking to integrate Algolia in my website. Will this be a lot of development work for me? What's the high level process look like?
Regards,
Leo

Hi Leo,
You can get value from Algolia [in as little as 45 seconds](https://youtu.be/IYY5RM1sBC0) by doing no more than:
- Upload a description of your data
- Paste three lines of code into the code for your website
Our business model is based on your continued success, so Algolia does provide additional tools and examples for customers who decide to go deeper.
You can determine when you're ready to explore additional integration, and we will be there to help.
