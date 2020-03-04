module coreir_reg_arst #(
    parameter width = 1,
    parameter arst_posedge = 1,
    parameter clk_posedge = 1,
    parameter init = 1
) (
    input clk,
    input arst,
    input [width-1:0] in,
    output [width-1:0] out
);
  reg [width-1:0] outReg;
  wire real_rst;
  assign real_rst = arst_posedge ? arst : ~arst;
  wire real_clk;
  assign real_clk = clk_posedge ? clk : ~clk;
  always @(posedge real_clk, posedge real_rst) begin
    if (real_rst) outReg <= init;
    else outReg <= in;
  end
  assign out = outReg;
endmodule

module commonlib_muxn__N2__width16 (
    input [15:0] in_data_0,
    input [15:0] in_data_1,
    input [0:0] in_sel,
    output [15:0] out
);
assign out = in_sel[0] ? in_data_1 : in_data_0;
endmodule

module Mux2xOutUInt16 (
    input [15:0] I0,
    input [15:0] I1,
    input S,
    output [15:0] O
);
commonlib_muxn__N2__width16 coreir_commonlib_mux2x16_inst0 (
    .in_data_0(I0),
    .in_data_1(I1),
    .in_sel(S),
    .out(O)
);
endmodule

module Counter_comb (
    input inc,
    input [15:0] self_count_O,
    output [15:0] O0,
    output [15:0] O1
);
Mux2xOutUInt16 Mux2xOutUInt16_inst0 (
    .I0(self_count_O),
    .I1(self_count_O + 16'h0001),
    .S(inc),
    .O(O0)
);
assign O1 = O0;
endmodule

module Counter (
    input inc,
    input CLK,
    input ASYNCRESET,
    output [15:0] O
);
wire [15:0] Counter_comb_inst0_O0;
wire [15:0] reg_PR_inst0_out;
Counter_comb Counter_comb_inst0 (
    .inc(inc),
    .self_count_O(reg_PR_inst0_out),
    .O0(Counter_comb_inst0_O0),
    .O1(O)
);
coreir_reg_arst #(
    .arst_posedge(1'b1),
    .clk_posedge(1'b1),
    .init(16'h0000),
    .width(16)
) reg_PR_inst0 (
    .clk(CLK),
    .arst(ASYNCRESET),
    .in(Counter_comb_inst0_O0),
    .out(reg_PR_inst0_out)
);
endmodule

