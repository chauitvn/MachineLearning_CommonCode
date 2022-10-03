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


git pull
git commit -m "Finish a feature"
git commit --amend

git fetch
Fetching downloads a branch from another repository, along with all of its associated commits and files. But, it doesn't try to integrate anything into your local repository. This gives you a chance to inspect changes before merging them with your project.

git push
git merge origin/GratheringData