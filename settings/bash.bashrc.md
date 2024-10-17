## Minhas Configurações

Aqui estão alguns dos aliases que uso para agilizar meu fluxo de trabalho em projetos Laravel e Git:

```bash
# Laravel Aliases
alias pa='php artisan'                                   # Atalho para o comando Artisan
alias pats='php artisan tenants:seed'                    # Semeia os dados para inquilinos
alias patm='php artisan tenants:migrate'                 # Executa migrações para inquilinos
alias patmf='php artisan tenants:migrate-fresh'          # Executa migrações frescas para inquilinos
alias resource='php artisan make:filament-resource'      # Cria um novo recurso Filament
alias serve='php artisan serve --port=8800'              # Inicia o servidor na porta 8800
alias pam='php artisan migrate'                           # Executa migrações
alias pamf='php artisan migrate:fresh'                   # Executa migrações frescas
alias model='php artisan make:model'                     # Cria um novo modelo
alias controller='php artisan make:controller'           # Cria um novo controlador

# Git Aliases
alias up='git add . && git commit -m "up"'               # Adiciona todas as alterações e faz um commit
alias push='git push origin'                              # Faz push para o repositório remoto
alias feature-s='git flow feature start'                  # Inicia uma nova feature no Git Flow
alias feature-f='git flow feature finish'                 # Finaliza uma feature no Git Flow
alias p-develop='git push origin develop'                 # Faz push para o branch develop
```
