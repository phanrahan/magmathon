// This should blink at a rate of ~ second

// 12mhz/(56000hz) = 214/2 = 107
// 12mhz/2400 = 5000 /2 = 2500
// 12mhz/9600 = 1250 /2 = 625
// 12mhz/38400 = 312 /2 = 156
// 12mhz/57600 =  208.3 /2 = 104
// 12mhz/19200 =  625 /2 = 312
// 12mhz/115200 =  104 /2 = 52

// 2400hz
//parameter UART_PERIOD = 5000;
//parameter UART_PERIOD_TH = 7500;  // three halves

//9600
//parameter UART_PERIOD = 1250;
//parameter UART_PERIOD_TH = 1875;  // three halves

//19200
//parameter UART_PERIOD = 625;
//parameter UART_PERIOD_TH = 937;  // three halves

//57600
//parameter UART_PERIOD = 206;
//parameter UART_PERIOD_TH = 309;  // three halves

// 115200
// * the trick here is to have the FPGA run slightly faster than the computer
// then the FPGA won't get behind and drop data.
parameter UART_PERIOD = 100;
parameter UART_PERIOD_TH = 150;  // three halves

module main (input CLK, input RX, output TX,
  output LED0,
  output LED1,
  output LED2,
  output LED3,
  output LED4,
  output PMOD_1,
  output PMOD_2);

  assign PMOD_1 = RX;
  assign PMOD_2 = TX;

  wire [7:0] readData;
  wire readValid;

  reg [7:0] readDataReg;
  wire txReady;
  reg txValid = 0;

  always @(posedge CLK) begin
    if(readValid) begin
      readDataReg <= readData;
      txValid <= 1;
    end else if(txReady) begin
      txValid <= 0;
    end
  end

  assign LED4 = readValid;
  assign {LED3, LED2, LED1, LED0} = readDataReg[3:0];

  RXMOD rxmod(.RX(RX), .CLK(CLK), .data(readData), .valid(readValid) );
  TXMOD txmod(.TX(TX), .CLK(CLK), .data(readDataReg+10), .valid(txValid), .ready(txReady) );
endmodule
