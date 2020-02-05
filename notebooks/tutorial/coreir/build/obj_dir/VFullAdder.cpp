// Verilated -*- C++ -*-
// DESCRIPTION: Verilator output: Design implementation internals
// See VFullAdder.h for the primary calling header

#include "VFullAdder.h"
#include "VFullAdder__Syms.h"


//--------------------
// STATIC VARIABLES


//--------------------

VL_CTOR_IMP(VFullAdder) {
    VFullAdder__Syms* __restrict vlSymsp = __VlSymsp = new VFullAdder__Syms(this, name());
    VFullAdder* __restrict vlTOPp VL_ATTR_UNUSED = vlSymsp->TOPp;
    // Reset internal values
    
    // Reset structure values
    _ctor_var_reset();
}

void VFullAdder::__Vconfigure(VFullAdder__Syms* vlSymsp, bool first) {
    if (0 && first) {}  // Prevent unused
    this->__VlSymsp = vlSymsp;
}

VFullAdder::~VFullAdder() {
    delete __VlSymsp; __VlSymsp=NULL;
}

//--------------------


void VFullAdder::eval() {
    VL_DEBUG_IF(VL_DBG_MSGF("+++++TOP Evaluate VFullAdder::eval\n"); );
    VFullAdder__Syms* __restrict vlSymsp = this->__VlSymsp;  // Setup global symbol table
    VFullAdder* __restrict vlTOPp VL_ATTR_UNUSED = vlSymsp->TOPp;
#ifdef VL_DEBUG
    // Debug assertions
    _eval_debug_assertions();
#endif  // VL_DEBUG
    // Initialize
    if (VL_UNLIKELY(!vlSymsp->__Vm_didInit)) _eval_initial_loop(vlSymsp);
    // Evaluate till stable
    int __VclockLoop = 0;
    QData __Vchange = 1;
    do {
        VL_DEBUG_IF(VL_DBG_MSGF("+ Clock loop\n"););
        _eval(vlSymsp);
        if (VL_UNLIKELY(++__VclockLoop > 100)) {
            // About to fail, so enable debug to see what's not settling.
            // Note you must run make with OPT=-DVL_DEBUG for debug prints.
            int __Vsaved_debug = Verilated::debug();
            Verilated::debug(1);
            __Vchange = _change_request(vlSymsp);
            Verilated::debug(__Vsaved_debug);
            VL_FATAL_MT("FullAdder.v", 13, "",
                "Verilated model didn't converge\n"
                "- See DIDNOTCONVERGE in the Verilator manual");
        } else {
            __Vchange = _change_request(vlSymsp);
        }
    } while (VL_UNLIKELY(__Vchange));
}

void VFullAdder::_eval_initial_loop(VFullAdder__Syms* __restrict vlSymsp) {
    vlSymsp->__Vm_didInit = true;
    _eval_initial(vlSymsp);
    // Evaluate till stable
    int __VclockLoop = 0;
    QData __Vchange = 1;
    do {
        _eval_settle(vlSymsp);
        _eval(vlSymsp);
        if (VL_UNLIKELY(++__VclockLoop > 100)) {
            // About to fail, so enable debug to see what's not settling.
            // Note you must run make with OPT=-DVL_DEBUG for debug prints.
            int __Vsaved_debug = Verilated::debug();
            Verilated::debug(1);
            __Vchange = _change_request(vlSymsp);
            Verilated::debug(__Vsaved_debug);
            VL_FATAL_MT("FullAdder.v", 13, "",
                "Verilated model didn't DC converge\n"
                "- See DIDNOTCONVERGE in the Verilator manual");
        } else {
            __Vchange = _change_request(vlSymsp);
        }
    } while (VL_UNLIKELY(__Vchange));
}

//--------------------
// Internal Methods

VL_INLINE_OPT void VFullAdder::_combo__TOP__1(VFullAdder__Syms* __restrict vlSymsp) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    VFullAdder::_combo__TOP__1\n"); );
    VFullAdder* __restrict vlTOPp VL_ATTR_UNUSED = vlSymsp->TOPp;
    // Body
    vlTOPp->COUT = ((((IData)(vlTOPp->I0) & (IData)(vlTOPp->I1)) 
                     | ((IData)(vlTOPp->I1) & (IData)(vlTOPp->CIN))) 
                    | ((IData)(vlTOPp->CIN) & (IData)(vlTOPp->I0)));
    vlTOPp->O = (((IData)(vlTOPp->I0) ^ (IData)(vlTOPp->I1)) 
                 ^ (IData)(vlTOPp->CIN));
}

void VFullAdder::_eval(VFullAdder__Syms* __restrict vlSymsp) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    VFullAdder::_eval\n"); );
    VFullAdder* __restrict vlTOPp VL_ATTR_UNUSED = vlSymsp->TOPp;
    // Body
    vlTOPp->_combo__TOP__1(vlSymsp);
}

void VFullAdder::_eval_initial(VFullAdder__Syms* __restrict vlSymsp) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    VFullAdder::_eval_initial\n"); );
    VFullAdder* __restrict vlTOPp VL_ATTR_UNUSED = vlSymsp->TOPp;
}

void VFullAdder::final() {
    VL_DEBUG_IF(VL_DBG_MSGF("+    VFullAdder::final\n"); );
    // Variables
    VFullAdder__Syms* __restrict vlSymsp = this->__VlSymsp;
    VFullAdder* __restrict vlTOPp VL_ATTR_UNUSED = vlSymsp->TOPp;
}

void VFullAdder::_eval_settle(VFullAdder__Syms* __restrict vlSymsp) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    VFullAdder::_eval_settle\n"); );
    VFullAdder* __restrict vlTOPp VL_ATTR_UNUSED = vlSymsp->TOPp;
    // Body
    vlTOPp->_combo__TOP__1(vlSymsp);
}

VL_INLINE_OPT QData VFullAdder::_change_request(VFullAdder__Syms* __restrict vlSymsp) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    VFullAdder::_change_request\n"); );
    VFullAdder* __restrict vlTOPp VL_ATTR_UNUSED = vlSymsp->TOPp;
    // Body
    // Change detection
    QData __req = false;  // Logically a bool
    return __req;
}

#ifdef VL_DEBUG
void VFullAdder::_eval_debug_assertions() {
    VL_DEBUG_IF(VL_DBG_MSGF("+    VFullAdder::_eval_debug_assertions\n"); );
    // Body
    if (VL_UNLIKELY((CIN & 0xfeU))) {
        Verilated::overWidthError("CIN");}
    if (VL_UNLIKELY((I0 & 0xfeU))) {
        Verilated::overWidthError("I0");}
    if (VL_UNLIKELY((I1 & 0xfeU))) {
        Verilated::overWidthError("I1");}
}
#endif  // VL_DEBUG

void VFullAdder::_ctor_var_reset() {
    VL_DEBUG_IF(VL_DBG_MSGF("+    VFullAdder::_ctor_var_reset\n"); );
    // Body
    CIN = VL_RAND_RESET_I(1);
    COUT = VL_RAND_RESET_I(1);
    I0 = VL_RAND_RESET_I(1);
    I1 = VL_RAND_RESET_I(1);
    O = VL_RAND_RESET_I(1);
}
