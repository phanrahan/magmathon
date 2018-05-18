module main (input [2:0] J1, output  D2, output  D1);
wire  inst0_O;
wire  inst1_O;
SB_LUT4 #(.LUT_INIT(16'h9696)) inst0 (.I0(J1[0]), .I1(J1[1]), .I2(J1[2]), .I3(1'b0), .O(inst0_O));
SB_LUT4 #(.LUT_INIT(16'hE8E8)) inst1 (.I0(J1[0]), .I1(J1[1]), .I2(J1[2]), .I3(1'b0), .O(inst1_O));
assign D2 = inst1_O;
assign D1 = inst0_O;
endmodule

