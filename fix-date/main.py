def run(input_date: str) -> str:
  def run(input_date: str, base_year: int = 1900) -> str:
    
    mes, dia, anio = input_date.split('/')

   
    dia = dia.zfill(2)
    mes = mes.zfill(2)

  
    anio_completo = str(base_year + int(anio))

    
    return f"{dia}-{mes}-{anio_completo}"


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
