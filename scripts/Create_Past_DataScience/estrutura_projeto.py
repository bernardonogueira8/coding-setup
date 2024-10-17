import os
import sys

def create_project_structure(project_path, project_name):
    project_name = "DataScience_" + project_name
    project_dir = os.path.join(project_path, project_name)

    # Criar diretório do projeto
    os.makedirs(project_dir, exist_ok=True)

    # Criar subdiretórios
    os.makedirs(os.path.join(project_dir, "1_notebooks", "0_raw"), exist_ok=True)
    os.makedirs(os.path.join(project_dir, "1_notebooks", "1_clean"), exist_ok=True)
    os.makedirs(os.path.join(project_dir, "1_notebooks", "2_processed"), exist_ok=True)

    os.makedirs(os.path.join(project_dir, "2_powerbi", "dashboards"), exist_ok=True)

    os.makedirs(os.path.join(project_dir, "3_docs"), exist_ok=True)

def create_project_streamlit(project_path, project_name):
    project_name = project_name + '_streamlit'
    project_dir = os.path.join(project_path, project_name)

    try:
        # Cria a pasta do projeto
        os.makedirs(project_dir)
        print(f"Pasta do projeto '{project_name}' criada em '{project_path}'.")

        # Caminhos dos arquivos a serem criados
        app_file_path = os.path.join(project_dir, 'app.py')
        requirements_file_path = os.path.join(project_dir, 'requirements.txt')

        # Cria o arquivo app.py
        with open(app_file_path, 'w') as app_file:
            app_file.write("# Arquivo principal do aplicativo Streamlit\n")
            app_file.write("import streamlit as st\n\n")
            app_file.write("st.title('Meu Projeto Streamlit')\n")
        print(f"Arquivo 'app.py' criado em '{project_dir}'.")

        # Cria o arquivo requirements.txt
        with open(requirements_file_path, 'w') as requirements_file:
            requirements_file.write("streamlit\n")
        print(f"Arquivo 'requirements.txt' criado em '{project_dir}'.")

    except Exception as e:
        print(f"Erro ao criar o projeto: {e}")

if __name__ == "__main__":

    project_name = input("Digite o nome do projeto: ")
    select_type = input("Tipo de projeto: (1-DataScience, 2-Streamlit): ")
    if select_type == '1':
        create_project_structure(project_path, project_name)
        print("Estrutura do projeto criada com sucesso!")
    elif select_type == '2':
        create_project_streamlit(project_path, project_name)
        print("Estrutura do projeto criada com sucesso!")
    else:
        print('Não entendi')


    input("Pressione Enter para sair...")