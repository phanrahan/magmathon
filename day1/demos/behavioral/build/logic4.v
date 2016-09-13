module main (input  S1, input  S2, input  S3, input  S4, output  D1);
wire  inst0_O;
SB_LUT4 #(.LUT_INIT(16'hAAAA)) inst0 (.I0(S1), .I1(S2), .I2(S3), .I3(S4), .O(inst0_O));
assign D1 = inst0_O;
endmodule

