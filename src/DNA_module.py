'''
NAME
    DNA_module
VERSION
    1.1
AUTHOR
    César Esparza
GITHUB
    https://github.com/cesparza2022/pythob_class.git
DESCRIPTION
    Herramientas para el manejo de secuencias de DNA
CATEGORY
    DNA sequence
 
 Functions
    validate
    frequency
    transcription
    reverse_complement
    purine_pirimidine
    


'''

nucleotides = ["A", "T","C","G"]
reverse_nucleotides = {"A":"T", "T":"A","C": "G","G":"C"}

#Pasa a mayúsculas y revisar que sean valores validos       
def validate(dna_seq):
  tmpseq = dna_seq.upper()
  for nuc in tmpseq:
    if nuc not in nucleotides:
      print("Esta mal el arreglo")
      return 
  return tmpseq
  
#Cuenta cuantas veces se repite cada nucleotido
def frequency(seq): 
  tmpFreqDict = {"A": 0, "C": 0, "G": 0, "T": 0}
  for nuc in seq: 
     if (nuc in tmpFreqDict): 
      tmpFreqDict[nuc] += 1
     else:
        tmpFreqDict[nuc] = 1 
  return tmpFreqDict

  #Cambia ADN a ARN
def transcription(seq):
  return seq.replace("T","U")

  # Saca la cadena complementaria  
def reverse_complement(seq):
  return"".join( reverse_nucleotides[nuc] for nuc in seq)

  #Regresa el porcentaje de 
def purine_pirimidine(seq, dec=0):
  
  a_num = seq.count('A') 
  t_num= seq.count('T')
  c_num= seq.count('C') 
  g_num = seq.count('G')

  long = len(seq) 
  
  if dec:
      at_content = round(( (a_num + t_num) / long)*100, dec) 
      cg_content = round(((c_num + g_num) / long)*100, dec) 
  else:
      at_content = (( a_num + t_num) / long) *100
      cg_content = ((c_num + g_num) / long) *100
     

  return at_content,cg_content

  #Asigna a una variable el contenido del archivo 
def return_seq(file_path):
  with open(file_path) as archivo:
    secuencia = archivo.read()
  
  return secuencia
  
