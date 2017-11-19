import pip

lista_paquetes = sorted([(p.key, p.version)
                        for p in pip.get_installed_distributions()])

print("{0:<30}{1:<30}".format('Nombre de Paquete', 'Versión'))
for paquete, version in lista_paquetes:
    print("{0:<30}{1:<30}".format(paquete, version))
