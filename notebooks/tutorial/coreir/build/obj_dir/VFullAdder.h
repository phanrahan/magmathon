// Verilated -*- C++ -*-
// DESCRIPTION: Verilator output: Primary design header
//
// This header should be included by all source files instantiating the design.
// The class here is then constructed to instantiate the design.
// See the Verilator manual for examples.

#ifndef _VFULLADDER_H_
#define _VFULLADDER_H_  // guard

#include "verilated.h"

class VFullAdder__Syms;

//----------

VL_MODULE(VFullAdder) {
  public:
    
    // PORTS
    // The application code writes and reads these signals to
    // propagate new values into/out from the Verilated model.
    VL_IN8(CIN,0,0);
    VL_OUT8(COUT,0,0);
    VL_IN8(I0,0,0);
    VL_IN8(I1,0,0);
    VL_OUT8(O,0,0);
    
    // LOCAL SIGNALS
    // Internals; generally not touched by application code
    
    // LOCAL VARIABLES
    // Internals; generally not touched by application code
    
    // INTERNAL VARIABLES
    // Internals; generally not touched by application code
    VFullAdder__Syms* __VlSymsp;  // Symbol table
    
    // PARAMETERS
    // Parameters marked /*verilator public*/ for use by application code
    
    // CONSTRUCTORS
  private:
    VL_UNCOPYABLE(VFullAdder);  ///< Copying not allowed
  public:
    /// Construct the model; called by application code
    /// The special name  may be used to make a wrapper with a
    /// single model invisible with respect to DPI scope names.
    VFullAdder(const char* name = "TOP");
    /// Destroy the model; called (often implicitly) by application code
    ~VFullAdder();
    
    // API METHODS
    /// Evaluate the model.  Application must call when inputs change.
    void eval();
    /// Simulation complete, run final blocks.  Application must call on completion.
    void final();
    
    // INTERNAL METHODS
  private:
    static void _eval_initial_loop(VFullAdder__Syms* __restrict vlSymsp);
  public:
    void __Vconfigure(VFullAdder__Syms* symsp, bool first);
  private:
    static QData _change_request(VFullAdder__Syms* __restrict vlSymsp);
  public:
    static void _combo__TOP__1(VFullAdder__Syms* __restrict vlSymsp);
  private:
    void _ctor_var_reset() VL_ATTR_COLD;
  public:
    static void _eval(VFullAdder__Syms* __restrict vlSymsp);
  private:
#ifdef VL_DEBUG
    void _eval_debug_assertions();
#endif  // VL_DEBUG
  public:
    static void _eval_initial(VFullAdder__Syms* __restrict vlSymsp) VL_ATTR_COLD;
    static void _eval_settle(VFullAdder__Syms* __restrict vlSymsp) VL_ATTR_COLD;
} VL_ATTR_ALIGNED(128);

#endif  // guard
