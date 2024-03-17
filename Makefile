.PHONY: install fmt lint

install:
	rye sync
	
lock:
	rye lock
	
fix:
	ruff check ocha --fix
	ruff format ocha

lint:
	ruff check ocha

publish:
ifndef v
	$(error version is undefined. specify v=x.x.x)
endif
ifneq ($(shell echo $(v) | grep -E '^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$$'), $(v))
	$(error Invalid version format. Expected format is from x.x.x to xxx.xxx.xxx)
endif
	git tag -a v$(v) -m "Publish Version $(v)"
	git push origin v$(v)
