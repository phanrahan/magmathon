module XOr3 (input [2:0] I, output  O);
wire  inst0_O;
SB_LUT4 #(.LUT_INIT(16'h9696)) inst0 (.I0(I[0]), .I1(I[1]), .I2(I[2]), .I3(1'b0), .O(inst0_O));
assign O = inst0_O;
endmodule

module And2 (input [1:0] I, output  O);
wire  inst0_O;
SB_LUT4 #(.LUT_INIT(16'h8888)) inst0 (.I0(I[0]), .I1(I[1]), .I2(1'b0), .I3(1'b0), .O(inst0_O));
assign O = inst0_O;
endmodule

module Or3 (input [2:0] I, output  O);
wire  inst0_O;
SB_LUT4 #(.LUT_INIT(16'hFEFE)) inst0 (.I0(I[0]), .I1(I[1]), .I2(I[2]), .I3(1'b0), .O(inst0_O));
assign O = inst0_O;
endmodule

module main (input  S1, input  S2, input  S3, output  D2, output  D1);
wire  inst0_O;
wire  inst1_O;
wire  inst2_O;
wire  inst3_O;
wire  inst4_O;
XOr3 inst0 (.I({S3,S2,S1}), .O(inst0_O));
And2 inst1 (.I({S2,S1}), .O(inst1_O));
And2 inst2 (.I({S3,S2}), .O(inst2_O));
And2 inst3 (.I({S1,S3}), .O(inst3_O));
Or3 inst4 (.I({inst3_O,inst2_O,inst1_O}), .O(inst4_O));
assign D2 = inst4_O;
assign D1 = inst0_O;
endmodule

