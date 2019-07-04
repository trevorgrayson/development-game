PYTHON="python3"
DEPDIR=".venv"

play: 
	@echo "What a terrible night for a curse."
	@$(PYTHON) -m play
	
compile: $(DEPDIR)
$(DEPDIR): requirements.txt
	$(PYTHON) -m pip install -t $(DEPDIR) -r requirements.txt

clean:
	rm -rf $(DEPDIR)
	find . -name "*.pyc" --delete
	find . -name "*.sw*" --delete

.PHONY: play
