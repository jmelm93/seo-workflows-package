### Package updates
> `python setup.py sdist bdist_wheel` # build package
> `twine check dist\*` # checks to ensure dist package setup properly for upload
> `python -m twine upload --repository-url htpps://test.pypi.org/legacy/ dist\*` # upload to pypi test site
> `python -m twine upload dist\*` # upload to pypi 
J6EGuDds6Mm_fmz