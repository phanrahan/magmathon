NAME = blink

BOARD = icestick

DEVICE = 1k
PCF = $(NAME).pcf

QUIET = -q

all: $(NAME).bin

%.bin: %.txt
	icepack $< $@

%.txt: %.blif
	arachne-pnr $(QUIET) -d $(DEVICE) -o $@ -p $(PCF) $< 

%.blif: %.v
	yosys $(QUIET) -p 'synth_ice40 -top main -blif $@' $<

%.v: %.py
	magma -b $(BOARD) -d "" $<

%.rpt: %.txt
	icetime -d hx$(DEVICE) -mtr $@ $<

upload: $(NAME).bin
	iceprog $<

explain: $(NAME).txt
	icebox_explain $<

clean:
	rm -f *.bin *.txt *.blif *.rpt *.v *.pcf


.PRECIOUS: %.bin %.txt %.blif 

.PHONY: all explain install clean
