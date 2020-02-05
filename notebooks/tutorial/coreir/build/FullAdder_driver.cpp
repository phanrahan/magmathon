#include "VFullAdder.h"
#include "verilated.h"
#include <iostream>
#include <fstream>
#include <verilated_vcd_c.h>
#include <sys/types.h>
#include <sys/stat.h>

// Based on https://www.veripool.org/projects/verilator/wiki/Manual-verilator#CONNECTING-TO-C
vluint64_t main_time = 0;       // Current simulation time
// This is a 64-bit integer to reduce wrap over issues and
// allow modulus.  You can also use a double, if you wish.

double sc_time_stamp () {       // Called by $time in Verilog
    return main_time;           // converts to double, to match
                                // what SystemC does
}

#if VM_TRACE
VerilatedVcdC* tracer;
#endif

void my_assert(
    unsigned int got,
    unsigned int expected,
    int i,
    const char* port) {
  if (got != expected) {
    std::cerr << std::endl;  // end the current line
    std::cerr << "Got      : 0x" << std::hex << got << std::endl;
    std::cerr << "Expected : 0x" << std::hex << expected << std::endl;
    std::cerr << "i        : " << std::dec << i << std::endl;
    std::cerr << "Port     : " << port << std::endl;
#if VM_TRACE
    // Dump one more timestep so we see the current values
    main_time++;
    tracer->dump(main_time);
    tracer->close();
#endif
    
    exit(1);
  }
}

int main(int argc, char **argv) {
  Verilated::commandArgs(argc, argv);
  VFullAdder* top = new VFullAdder;
  
#if VM_TRACE
  Verilated::traceEverOn(true);
  tracer = new VerilatedVcdC;
  top->trace(tracer, 99);
  mkdir("logs", S_IRWXU | S_IRWXG | S_IROTH | S_IXOTH);
  tracer->open("logs/FullAdder.vcd");
#endif

  top->I0 = 1;
  top->I1 = 1;
  top->CIN = 1;
  top->eval();
  main_time++;
  #if VM_TRACE
  tracer->dump(main_time);
  #endif
  my_assert(top->O, 1 & 1, 4, "FullAdder.O");
  my_assert(top->COUT, 1 & 1, 5, "FullAdder.COUT");


#if VM_TRACE
  tracer->close();
#endif
  
}
