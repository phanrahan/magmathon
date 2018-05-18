module Add (input  A, input  B, output  S, output  C);
    assign S = A ^ B;
    assign C = A & B;
endmodule

module main (input [1:0] J1, output [1:0] J3, input  CLKIN);
wire  inst0_S;
wire  inst0_C;
Add inst0 (.A(J1[0]), .B(J1[1]), .S(inst0_S), .C(inst0_C));
assign J3 = {inst0_C,inst0_S};
endmodule

