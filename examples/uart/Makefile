all: out/uart_main.bin

clean:
	\rm -rf out/*

out/%.blif: %.v
	mkdir -p out
	yosys -q -p 'synth_ice40 -top main -blif $@' txmod.v rxmod.v $<

out/%_pnr.txt: out/%.blif
	arachne-pnr -q -d 1k -o $@ -p ice40.pcf $<

out/%.bin: out/%_pnr.txt
	icepack $< $@

%.run: out/%.bin
	iceprog $<
