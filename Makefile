PYTHON="python3"
DEPDIR=".venv"

play: 
	@echo "What a terrible night for a curse."
	@$(PYTHON) -m play
	@git commit players.tsv -m "SCORE!"
	@git push origin master # fishing
	
compile: $(DEPDIR)
$(DEPDIR): requirements.txt
	$(PYTHON) -m pip install -t $(DEPDIR) -r requirements.txt

console:
	$(PYTHON) -m console

clean:
	rm -rf $(DEPDIR)
	find . -name "*.pyc" --delete
	find . -name "*.sw*" --delete

.PHONY: play console
