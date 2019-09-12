PYTHON="python3"
DEPDIR=".venv"

export PYTHONPATH = .:$(DEPDIR)

play: 
	@echo "What a terrible night for a curse."
	@$(PYTHON) -m play
	@git commit players.tsv -m "SCORE!"
	@git push origin master # fishing
	
compile: $(DEPDIR)/updatetime
$(DEPDIR)/updatetime: requirements.txt
	mkdir -p logs
	$(PYTHON) -m pip install -t $(DEPDIR) -r requirements.txt
	touch $(DEPDIR)/updatetime

server: compile
	@$(PYTHON) -m terminal

console: compile
	@$(PYTHON) -m console

curse: compile
	@$(PYTHON) -m curse $(GAME)

clean:
	rm -rf $(DEPDIR)
	find . -name "*.pyc" -delete
	find . -name "*.sw*" -delete

.PHONY: play console terminal curse
