

.. note:: "Improving the process is more important than doing the work. If you have to choose between improving the process and doing the work, always choose to improve the process. " --Eliahu Goldratt, The Goal


Since it is Closember, I thought it would be good to drop a few items here.
Closember is the antidote to the Hacktoberfest hangover. closember.org

Maintainers are the pollinators of open source
===============================================

They work for free to make your products useful. They are closer to your customers than you could ever be.
They are human too, and might not have acess to resources for optimization.

Symptoms of an unhealthy repo
==============================

Contributor churn (lots of 1 commit contribs)
Ratio of Issues to PRs
Long cycle times for PR approval, issue closing
Falling behind upstream dependencies.
Red Herring: Lack of activity may not indicate poor health.


Few downstream dependencies
----------------------------

Indicated by stars, followers, forks "used-by" badges and dependency graphs.
https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/exploring-the-dependencies-of-a-repository


Attracting more pollinators
=============================

Students,
retirees
downstream dependents

DEI makes the funnel wider
----------------------------

Accessibility, I18N make it easier for "under-represented" communities to participate.


Badges!
--------

Participation badges for personal profiles. https://badges.fedoraproject.org/
PDFs to download certs and posters.

Quality badges for repositories and branches.
https://github.com/eltorocorp/badgeserver
https://shields.io/category/coverage


Automate to reduce toil
------------------------

Automating the inspection of merge requests is the path to reducing maintainer toil. The SKA telescope team knows this well: https://developer.skatelescope.org/en/latest/tools/git.html#merge-request-quality-checks


Pre-Push hooks to fail close
-----------------------------

Using linters and test runners. https://pre-commit.com/


Arrange tests in order of commits
-----------------------------------

Commit that introduces a failing test using pytest.mark.xfail.
https://github.com/seddonym/import-linter/pull/65/commits/91b3f27c6f4efa528c088fde0d78b1c939902c7e

Follow up commit that causes the test to pass (notice the removal of the xfail).
https://github.com/seddonym/import-linter/pull/65/commits/0d4ed65f3478307a1055dcef4d487f3f1218dd1d



Signed PRs
----------

Make it easier for new contribs to set up their keys and git clients.



Appendix
--------------


https://github.com/mitodl/ol-data-pipelines/blob/main/src/ol_data_pipelines/lib/file_rendering.py

https://github.com/mitodl/ol-infrastructure



Internet lifer, recovering sales engineer, open source servant.
