module XOr2 (input [1:0] I, output  O);
wire  inst0_O;
SB_LUT4 #(.LUT_INIT(16'h6666)) inst0 (.I0(I[0]), .I1(I[1]), .I2(1'b0), .I3(1'b0), .O(inst0_O));
assign O = inst0_O;
endmodule

module main (input  J1, output  D1, input  CLKIN);
wire  inst0_Q;
wire  inst1_O;
SB_DFF inst0 (.C(CLKIN), .D(inst1_O), .Q(inst0_Q));
XOr2 inst1 (.I({inst0_Q,J1}), .O(inst1_O));
assign D1 = inst0_Q;
endmodule

