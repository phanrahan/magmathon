module Register2 (input [1:0] I, input  CLK, output [1:0] O);
wire  inst0_Q;
wire  inst1_Q;
SB_DFF inst0 (.C(CLK), .D(I[0]), .Q(inst0_Q));
SB_DFF inst1 (.C(CLK), .D(I[1]), .Q(inst1_Q));
assign O = {inst1_Q,inst0_Q};
endmodule

module main (input  S1, input  S2, output  D2, output  D1, input  CLKIN);
wire [1:0] inst0_O;
Register2 inst0 (.I({S2,S1}), .CLK(CLKIN), .O(inst0_O));
assign D2 = inst0_O[1];
assign D1 = inst0_O[0];
endmodule

