#
all:  students.html education.html software.html cv_publications.html opendata.html

%.html: %.rst
	python3 converter.py $*.rst > tmp.rst
	rst2html tmp.rst > tmp.html

	python3 converter.py tmp.html > $*.html
	rm tmp.rst tmp.html
