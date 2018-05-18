module main (input [7:0] J1, output [3:0] J3, input  CLKIN);
wire  inst0_O;
wire  inst1_O;
wire  inst2_O;
wire  inst3_O;
SB_LUT4 #(.LUT_INIT(16'h8888)) inst0 (.I0(J1[0]), .I1(J1[4]), .I2(1'b0), .I3(1'b0), .O(inst0_O));
SB_LUT4 #(.LUT_INIT(16'h8888)) inst1 (.I0(J1[1]), .I1(J1[5]), .I2(1'b0), .I3(1'b0), .O(inst1_O));
SB_LUT4 #(.LUT_INIT(16'h8888)) inst2 (.I0(J1[2]), .I1(J1[6]), .I2(1'b0), .I3(1'b0), .O(inst2_O));
SB_LUT4 #(.LUT_INIT(16'h8888)) inst3 (.I0(J1[3]), .I1(J1[7]), .I2(1'b0), .I3(1'b0), .O(inst3_O));
assign J3 = {inst3_O,inst2_O,inst1_O,inst0_O};
endmodule

