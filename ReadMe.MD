1. Create a new vitual environment
python -m venv D:\OutsourceViet\SourceCode\MachineLearning_CommonCode\venv
2. Install the required package
pip freeze
pip install -r requirements.txt

========================================
tra ve json object
serializers.serialize('json', all_items, fields=('key','value', "HasActive"))


#################Git Command###########################
https://www.atlassian.com/git/glossary

---------Git Branch--------------------------------
https://www.atlassian.com/git/tutorials/using-branches/git-merge
1. Preparing to merge
Before performing a merge there are a couple of preparation steps to take to ensure the merge goes smoothly.
2. Confirm the receiving branch
Execute git status to ensure that HEAD is pointing to the correct merge-receiving branch. 

[code]git status[code]

If needed, execute git checkout to switch to the receiving branch. In our case we will execute .

[code]git checkout main[code]

3. Fetch latest remote commits
Make sure the receiving branch and the merging branch are up-to-date with the latest remote changes. Execute git fetch to pull the latest remote commits. Once the fetch is completed ensure the main branch has the latest updates by executing git pull.

[code]git pull[/code]

4. Merging
Once the previously discussed "preparing to merge" steps have been taken a merge can be initiated by executing git merge where  is the name of the branch that will be merged into the receiving branch.

[code]git merge[/code]

5. Fast Forward Merge

git commit -m "Finish a feature"
git commit --amend

git fetch
Fetching downloads a branch from another repository, along with all of its associated commits and files. But, it doesn't try to integrate anything into your local repository. This gives you a chance to inspect changes before merging them with your project.

git push
git merge origin/GratheringData