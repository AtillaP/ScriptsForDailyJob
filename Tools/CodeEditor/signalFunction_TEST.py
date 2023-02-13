from signalFunction import SigFunc

TEST_input = [
    "uint8 PUT_DSR_QFK_Art2(void)",
    "{ /* { } */",
    "   uint8 tx_signal;",
    "",
    "   tx_signal = 0U;",
    "   return tx_signal;",
    "}",
    "",
    "/**",
    "@ingroup DSR_01_XIX_MQB2020_FCANFD",
    "@brief @b Signal: DSR_QFK_KruemmSoll_VZ_XIX_DSR_01_XIX_MQB2020_FCANFD",
    "@satisfies ",
    "@par Signal position:",
    "Length: 1, Byte: 4, Bit: 7, byte order: intel",
    "@details",
    "Signal description...",
    "@param 0 .. 1 Unit: , Offset: 0, LSB: 0, init: 0",
    "*/",
    "boolean PUT_DSR_QFK_KruemmSoll_VZ(void)",
    "{",
    "   boolean tx_signal = False;",
    "",
    "   #if(FEAT_CFG_FUNCTION_DSR_CONFMODE)",
    "   if((Get_dsr_curvature_request()) < 0)",
    "   {",
    "      tx_signal = True;",
    "   }",
    "   #endif",
    "",
    "   return(tx_signal);",
    "}"
]



def Main():
    #for i in TEST_input: print(i)
    #sf = SigFunc('PUT_DSR_QFK_KruemmSoll_VZ', 'DSR_01')
    #sf.setSignalDefinition(TEST_input, 18)
    #sf.setOutPutFile('output.txt')
    #sf.printSignalToFile()
    #for i in sf.signalDefinition: print(i)
    #for i in TEST_input[18:]: print(i)
    for i in TEST_input: print(i.count('{'))

if __name__ == '__main__':
    Main()