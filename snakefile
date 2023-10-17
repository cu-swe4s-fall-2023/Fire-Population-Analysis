COUNTRIES = ['Albania', 'Italy', 'Canada']

rule all:
    input:
        expand('{country}.png', country=COUNTRIES)

rule download_data:
    output:
        'Agrofood_co2_emission.csv'
    shell:
        'wget -O {output} "https://docs.google.com/uc?export=download&id=1Wytf3ryf9EtOwaloms8HEzLG0yjtRqxr"'        
        
rule get_data:
    input:
        'Agrofood_co2_emission.csv'
    output:
        '{x}.txt'
    shell: 
        'python get_data.py {input} {wildcards.x} {output}'
        
rule plot_data:
    input:
        '{w}.txt'
    output:
        '{w}.png'
    shell:
        'python hist.py {input} {output} {wildcards.w} Fires Freq.'