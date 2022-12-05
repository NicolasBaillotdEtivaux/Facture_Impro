#!/usr/bin/env python3

################################################################################
# blabla ...
################################################################################

# imported packages:
import os
import numpy as np

def main():

    invoice_name = 'factures/facture_03-2022.txt'
    
    ############################################################################
    # Solution with bad copy/paste form:

    # customer = 'LUDI'
    
    # with open(invoice_name,'r') as f:
    #     raw_table = f.read()
    #     # split the head of the table from the content:
    #     head, content = raw_table.split('PRIX')[0], raw_table.split('PRIX')[1]
    #     # clean the data:
    #     content = content.split('EN')[0]
    #     content = content.split()
    #     # get the total and remove it from the data:
    #     total = content[-2]+r' \euro'
    #     content = content[:-2]

    #     # get the lines from the data:
    #     lines = []
        
    #     item_count = 0
    #     line = []
    #     for item in content:
    #         if not item_count == 8:
    #             line.append(item)
    #             item_count += 1
    #         else:
    #             line.append(item)
    #             lines.append(line)
    #             line = []
    #             item_count = 0


    ############################################################################
    with open(invoice_name,'r') as f:
        raw_table = f.read()
        print(f)

    
    ############################################################################
    # Generate the invoice in pdf format via pdflatex:

    # invoice_tex = invoice_name.split('.txt')[0]+'.tex'
    
    # with open(invoice_tex, 'w') as invoice:

    #     # Header of the latex file:
    #     invoice.write(r'\documentclass{article}')
    #     invoice.write('\n')
    #     invoice.write(r'\usepackage[utf8]{inputenc}')
    #     invoice.write('\n')
    #     invoice.write(r'\usepackage{eurosym}')
    #     invoice.write('\n')
    #     invoice.write(r'\usepackage[colorlinks]{hyperref}')
    #     invoice.write('\n')
    #     invoice.write(r'\usepackage[left=1in,top=1in,right=1in,bottom=1in]{geometry} % Document margins')
    #     invoice.write('\n')
    #     invoice.write(r'\usepackage{graphicx}')
    #     invoice.write('\n')
    #     invoice.write(r'\usepackage{tabularx}')
    #     invoice.write('\n')
    #     invoice.write(r'\usepackage{multirow}')
    #     invoice.write('\n')
    #     invoice.write(r'\usepackage{ragged2e}')
    #     invoice.write('\n')
    #     invoice.write(r'\usepackage{hhline}')
    #     invoice.write('\n')
    #     invoice.write(r'\usepackage{array}')
    #     invoice.write('\n')
    #     invoice.write(r'\usepackage[francais]{babel}')
    #     invoice.write('\n')
    #     invoice.write(r'\usepackage[T1]{fontenc}')
    #     invoice.write('\n')
    #     invoice.write(r'\usepackage{lmodern}')

    #     invoice.write('\n')
    #     invoice.write('\n')

    #     invoice.write(r'\hypersetup{urlcolor=blue}')
    #     invoice.write('\n')
    #     invoice.write(r'\newcolumntype{R}[1]{>{\raggedleft\let\newline\\\arraybackslash\hspace{0pt}}m{#1}}')
    #     invoice.write('\n')
    #     invoice.write('\n')

    #     invoice.write(r'\begin{document}')
    #     invoice.write('\n')
    #     invoice.write(r'\thispagestyle{empty}')
    #     invoice.write('\n')

    #     # Content of the invoice:
    #     invoice.write(r'% Header, for company, invoice info')
    #     invoice.write('\n')
    #     invoice.write(r'\begin{tabularx}{\textwidth}{l X l}')
    #     invoice.write('\n')
    #     invoice.write(r'\hspace{-8pt} \multirow{5}{*}{\includegraphics[height=1.98cm]{logo.png}} & \textbf{Léa Chapellier} & \hskip12pt\multirow{5}{*}{\begin{tabular}{r} \footnotesize\bf DATE \\[-0.8ex] \footnotesize \MakeUppercase{\today} \\ \end{tabular}}\hspace{-6pt} \\')
    #     invoice.write('\n')
    #     invoice.write(r'& \bf{Formatrice en Théâtre improvisé}& \\')
    #     invoice.write('\n')
    #     invoice.write(r'& 16 rue Roubichou, 31500 Toulouse & \\')
    #     invoice.write('\n')
    #     invoice.write(r'& 07 55 62 82 85 & \\')
    #     invoice.write('\n')
    #     invoice.write(r'& \href{lea.chapellier@outlook.com} & \\')
    #     invoice.write('\n')
    #     invoice.write(r'& SIRET: 321 289 456 00014 & \\')
    #     invoice.write('\n')
    #     invoice.write(r'\end{tabularx} ')
    #     invoice.write('\n')
    #     invoice.write('\n')
    #     invoice.write(r'\vspace{1 cm}')
    #     invoice.write('\n')
    #     invoice.write('\n')
    #     invoice.write(r'Devis adressé à:')
    #     invoice.write('\n')
    #     invoice.write(r'\vspace{0.1cm}')
    #     invoice.write('\n')
    #     invoice.write('\n')
    #     invoice.write(r'\vspace{0.5cm}')
        
    #     # Customer:
    #     invoice.write(r'\Large\textbf{'+f'{customer}'+r'}\normalsize')

        
    #     invoice.write('\n')
    #     invoice.write('\n')
    #     invoice.write(r'\begin{table}[h!]')
    #     invoice.write('\n')
    #     invoice.write(r'\begin{tabular}{c c c c c c c}')
    #     invoice.write('\n')
    #     invoice.write(r'\hline \\[0.25cm]')
    #     invoice.write('\n')
    #     invoice.write(r"\centering{\bf{Date}} & \centering{\bf{Désignation}} & \centering{\bf{Heure début}} & \centering{\bf{Heure fin}} & \centering{\bf{Tarif horaire}} & \centering{\bf{Nbr d'heure}} & \bf Prix \\")
    #     invoice.write('\n')
    #     invoice.write(r'& & & & (TTC) & & (TTC)\\[0.25cm]\hline \\')
    #     invoice.write('\n')

        
        
    #     # write the data into the table:
    #     for line in lines:
    #         for i, item in enumerate(line):
    #             # change the euro symbol to avoid encoding problems:
    #             if item == '€':
    #                 item = '\euro'
    #             if i == len(line) - 1:
    #                 invoice.write(f' {item} ')
    #                 invoice.write(r'\\[0.25cm]')
    #                 invoice.write('\n')
    #             elif line[i+1] == '€':
    #                 invoice.write(f' {item} ')
    #             else:
    #                 invoice.write(f' {item} & ')

    #     invoice.write(r'\hline \\')
    #     invoice.write('\n')
    #     invoice.write(r'& & & & & \bf{Total TTC:} & ')
    #     invoice.write(r'\bf{'+f'{total}'+'}')

        
    #     invoice.write('\n')
    #     invoice.write(r'\end{tabular}')
    #     invoice.write('\n')
    #     invoice.write(r'\end{table}')



    #     invoice.write('\n')
    #     invoice.write(r'\end{document}')


    # Compile le latex file and generates the pdf:
    # os.system(f'pdflatex {invoice_tex}')


    ############################################################################
    # Solution with docx api:
    
    # from docx.api import Document

    # # Load the first table from your document. In your example file,
    # # there is only one table, so I just grab the first one.
    # document = Document('facture_test.docx')
    # table = document.tables[0]

    # # Data will be a list of rows represented as dictionaries
    # # containing each row's data.
    # data = []

    # keys = None
    # for i, row in enumerate(table.rows):
    #     text = (cell.text for cell in row.cells)

    #     # Establish the mapping based on the first row
    #     # headers; these will become the keys of our dictionary
    #     if i == 0:
    #         keys = tuple(text)
    #         continue

    #     # Construct a dictionary for this row, mapping
    #     # keys to values for this row
    #     row_data = dict(zip(keys, text))
    #     data.append(row_data)

if __name__ == "__main__":
    main()
