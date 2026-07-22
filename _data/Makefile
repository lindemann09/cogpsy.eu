#
all:  students.html education.html software.html cv_publications.html opendata.html

%.html: %.rst
	uv run converter.py $*.rst > tmp.rst
	uv tool run --from docutils rst2html tmp.rst > tmp.html

	uv run converter.py tmp.html > $*.html
	rm tmp.rst tmp.html
