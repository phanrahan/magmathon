module main (input  S1, input  S2, input  S3, output  D2, output  D1);
wire  inst0_O;
wire  inst1_O;
SB_LUT4 #(.LUT_INIT(16'h9696)) inst0 (.I0(S1), .I1(S2), .I2(S3), .I3(1'b0), .O(inst0_O));
SB_LUT4 #(.LUT_INIT(16'hE8E8)) inst1 (.I0(S1), .I1(S2), .I2(S3), .I3(1'b0), .O(inst1_O));
assign D2 = inst1_O;
assign D1 = inst0_O;
endmodule

