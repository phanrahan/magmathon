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

module coreir_mux #(
    parameter width = 1
) (
    input [width-1:0] in0,
    input [width-1:0] in1,
    input sel,
    output [width-1:0] out
);
  assign out = sel ? in1 : in0;
endmodule

module coreir_const #(
    parameter width = 1,
    parameter value = 1
) (
    output [width-1:0] out
);
  assign out = value;
endmodule

module coreir_add #(
    parameter width = 1
) (
    input [width-1:0] in0,
    input [width-1:0] in1,
    output [width-1:0] out
);
  assign out = in0 + in1;
endmodule

module commonlib_muxn__N2__width16 (
    input [15:0] in_data_0,
    input [15:0] in_data_1,
    input [0:0] in_sel,
    output [15:0] out
);
wire [15:0] _join_out;
coreir_mux #(
    .width(16)
) _join (
    .in0(in_data_0),
    .in1(in_data_1),
    .sel(in_sel[0]),
    .out(_join_out)
);
assign out = _join_out;
endmodule

module Mux2xOutUInt16 (
    input [15:0] I0,
    input [15:0] I1,
    input S,
    output [15:0] O
);
wire [15:0] coreir_commonlib_mux2x16_inst0_out;
commonlib_muxn__N2__width16 coreir_commonlib_mux2x16_inst0 (
    .in_data_0(I0),
    .in_data_1(I1),
    .in_sel(S),
    .out(coreir_commonlib_mux2x16_inst0_out)
);
assign O = coreir_commonlib_mux2x16_inst0_out;
endmodule

module Counter_comb (
    input inc,
    input [15:0] self_count_O,
    output [15:0] O0,
    output [15:0] O1
);
wire [15:0] Mux2xOutUInt16_inst0_O;
wire [15:0] const_1_16_out;
wire [15:0] magma_Bits_16_add_inst0_out;
Mux2xOutUInt16 Mux2xOutUInt16_inst0 (
    .I0(self_count_O),
    .I1(magma_Bits_16_add_inst0_out),
    .S(inc),
    .O(Mux2xOutUInt16_inst0_O)
);
coreir_const #(
    .value(16'h0001),
    .width(16)
) const_1_16 (
    .out(const_1_16_out)
);
coreir_add #(
    .width(16)
) magma_Bits_16_add_inst0 (
    .in0(self_count_O),
    .in1(const_1_16_out),
    .out(magma_Bits_16_add_inst0_out)
);
assign O0 = Mux2xOutUInt16_inst0_O;
assign O1 = Mux2xOutUInt16_inst0_O;
endmodule

module Counter (
    input inc,
    input CLK,
    input ASYNCRESET,
    output [15:0] O
);
wire [15:0] Counter_comb_inst0_O0;
wire [15:0] Counter_comb_inst0_O1;
wire [15:0] reg_PR_inst0_out;
Counter_comb Counter_comb_inst0 (
    .inc(inc),
    .self_count_O(reg_PR_inst0_out),
    .O0(Counter_comb_inst0_O0),
    .O1(Counter_comb_inst0_O1)
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
assign O = Counter_comb_inst0_O1;
endmodule

