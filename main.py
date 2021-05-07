import pandas as pd

def dar_formato(txt, total, tipo):
    if len(txt) + 1 <= total:
        resto = total - len(txt)
        if tipo == 'A':
            txt = txt + ' ' * resto
        elif tipo == 'N':
            txt = '0' * resto + txt

    if len(txt) > total:
        txt = txt[:total]

    return txt

def main():

    col_list = ['MONTO', 'FECHA', 'Rango de texto']
    df_excel = pd.read_excel("TABLERO RESPUESTA BANCO.xlsx", usecols=col_list, sheet_name='RESPUESTA BANCO')

    txt = ""
    periodo = input("Ingrese el período (AAAAMM): ")
    #CABECERA
    txt += "01"                         #1  TIPO CABECERA
    txt += "00000001"                   #2  SECUENCIA CABECERA
    total = df_excel['MONTO'].sum() 
    print(total)    
    txt += dar_formato(str(total), 12, 'N')  #3  IMPORTE TOTAL CABECERA
    txt += '98'                         #4  CÓDIGO CABECERA
    txt += dar_formato('', 13, 'N')     #5  BLANCOS
    txt += '020'                        #6  BANCO CABECERA
    txt += periodo                      #7  PERÍODO DE CABECERA
    txt += '0000'                       #8  BLANCOS
    cantidad = str(df_excel.shape[0])
    txt += dar_formato(cantidad, 7, 'N')#9  CANTIDAD DE REGISTROS DE CABECERA
    txt += 'P'                          #10 FORMA DE PAGO CABECERA
    txt += 'M'                          #11 TIPO PAGO CABECERA
    txt += '2'                          #12 TIPO ESPECIAL CABECERA
    txt += 'LUQUI'                      #13 TIPO LEYENDA CABECERA
    txt += '00000'                      #14 BLANCOS

    #CUERPO
    for index, row in df_excel.iterrows():
        txt += "\n01"                                     #1  TIPO DETALLE
        txt += dar_formato(str(index), 8, "N")          #2  SECUENCIA DETALLE
        txt += dar_formato(str(row["MONTO"]), 12, 'N')  #3  IMPORTE TOTAL DETALLE
        print(str(row["MONTO"]))
        txt += '00'                                     #4  CUENTA DETALLE
        txt += 'P'                                      #5  MARCA DETALLE
        fecha = str(row['FECHA'])
        print(fecha)                   
        dia = fecha[6:]
        mes = fecha[4:6]
        año = fecha[:4]
        txt += dia + mes + año                          #6  FECHA DE PAGO DETALLE
        txt += '00'                                     #7  EX CAJA DETALLE
        txt += '0'                                      #8  TIPO BENEFICIARIO DETALLE
        dni = str(row['Rango de texto'])
        txt += dar_formato(dni, 8, 'N')                 #9  NUMERO BENFICIARIO DETALLE Y 10 COPART DETALLE (DNI)
        txt += periodo[4:] + periodo[2:4]               #11 PERÍODO PAGO DETALLE
        txt += '0'                                      #12 TIPO PAGO DETALLE
        txt += '020'                                    #13 BANCO PAGADOR DETALLE
        txt += '302'                                    #14 AGENCIA PAGADORA DETALLE
        txt += '0'                                      #15 DIGITO B DETALLE
        txt += '0'                                      #16 DIGITO A DETALLE
        txt += '0'                                      #17 DIGITO I DETALLE
        txt += '0000001'                                #18 NRO. COMPROBANTE DETALLE
        txt += '0'                                      #19 MOTIVO PAGO/IMPAGOS DETALLE
        txt += '0000'                                   #20 BLANCOS
    
    f = open("TABLERO RESPUESTA BANCO.txt", "w")
    f.write(txt)
    f.close()

if __name__ == "__main__":
    main()