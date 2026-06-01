run:
	python src/pipeline.py

clean:
	rm -rf __pycache__

git:
	git add .
	git commit -m "update"
	git push
