## Minhas Configurações

Local do arquivo:
`C:\Program Files\Git\etc\bash.bashrc`.

Aqui estão alguns dos aliases que uso para agilizar meu fluxo de trabalho em projetos Laravel e Git:

```bash
# Outras Configurações Python
alias run-s = 'streamlit run streamlit_app.py'           # Rodando codigo Streamlit

# Laravel Aliases
alias pa='php artisan'                                   # Atalho para o comando Artisan
alias serve='php artisan serve --host=localhost'         # Inicia o servidor na porta 8800
alias pam='php artisan migrate'                          # Executa migrações
alias pamf='php artisan migrate:fresh'                   # Executa migrações frescas
alias model='php artisan make:model'                     # Cria um novo modelo
alias controller='php artisan make:controller'           # Cria um novo controlador

# TenancyforLaravel Aliases
alias pats='php artisan tenants:seed'                    # Semeia os dados para inquilinos
alias patm='php artisan tenants:migrate'                 # Executa migrações para inquilinos
alias patmf='php artisan tenants:migrate-fresh'          # Executa migrações frescas para inquilinos

# Filament Aliases
alias resource='php artisan make:filament-resource --view'                                  # Cria um novo recurso Filament
alias resource-g='php artisan make:filament-resourc --view --generate'                      # Cria um novo recurso Filament com generate
alias resource-s='php artisan make:filament-resource --view --generate --soft-deletes'      # Cria um novo recurso Filament com soft deletes
alias shield-all='php artisan shield:generate --all'                                        # Gera todoas as politicas e validações

# Git Aliases
alias up='git add . && git commit -m "up"'                # Adiciona todas as alterações e faz um commit
alias add='git add . && git commit -m '                   # Redução de add . e commit, commit -am buga muito 
alias push='git push origin'                              # Faz push para o repositório remoto
alias feature-s='git flow feature start'                  # Inicia uma nova feature no Git Flow
alias feature-f='git flow feature finish'                 # Finaliza uma feature no Git Flow
alias p-develop='git push origin develop'                 # Faz push para o branch develop
alias user-f='php artisan make:filament-user'             # Criar usuario filament


```
