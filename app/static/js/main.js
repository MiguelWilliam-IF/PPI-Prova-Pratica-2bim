document.addEventListener('DOMContentLoaded', function() {
    // Auto-hide alerts after 5 seconds
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(function(alert) {
        setTimeout(function() {
            const bsAlert = new bootstrap.Alert(alert);
            if (bsAlert) {
                bsAlert.close();
            }
        }, 5000);
    });

    // Confirmação de exclusão melhorada
    const deleteButtons = document.querySelectorAll('button[onclick*="confirm"]');
    deleteButtons.forEach(function(button) {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            const form = this.closest('form');
            
            // Criar modal de confirmação customizado
            const modal = createConfirmModal(
                'Confirmar Exclusão',
                'Tem certeza que deseja excluir este item? Esta ação não pode ser desfeita.',
                function() {
                    form.submit();
                }
            );
            modal.show();
        });
    });

    // Validação em tempo real dos forms
    const forms = document.querySelectorAll('form');
    forms.forEach(function(form) {
        form.addEventListener('input', function(e) {
            validateField(e.target);
        });
    });

    // Validação especial para jogos (times diferentes)
    const timeCasaSelect = document.querySelector('select[name="time_casa_id"]');
    const timeVisitanteSelect = document.querySelector('select[name="time_visitante_id"]');
    
    if (timeCasaSelect && timeVisitanteSelect) {
        [timeCasaSelect, timeVisitanteSelect].forEach(function(select) {
            select.addEventListener('change', function() {
                validateDifferentTeams();
            });
        });
    }
});

// Função para criar modal de confirmação
function createConfirmModal(title, message, confirmCallback) {
    const modalHtml = `
        <div class="modal fade" id="confirmModal" tabindex="-1">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title">${title}</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
                    </div>
                    <div class="modal-body">
                        <p>${message}</p>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancelar</button>
                        <button type="button" class="btn btn-danger" id="confirmBtn">Confirmar</button>
                    </div>
                </div>
            </div>
        </div>
    `;
    
    // Remove modal existente se houver
    const existingModal = document.getElementById('confirmModal');
    if (existingModal) {
        existingModal.remove();
    }
    
    // Adiciona novo modal
    document.body.insertAdjacentHTML('beforeend', modalHtml);
    const modal = new bootstrap.Modal(document.getElementById('confirmModal'));
    
    // Adiciona event listener para o botão de confirmação
    document.getElementById('confirmBtn').addEventListener('click', function() {
        confirmCallback();
        modal.hide();
    });
    
    return modal;
}

// Validação de campo em tempo real
function validateField(field) {
    const fieldName = field.name;
    const fieldValue = field.value.trim();
    
    // Remove classes de validação anteriores
    field.classList.remove('is-valid', 'is-invalid');
    
    // Validações específicas
    switch(fieldName) {
        case 'nome':
            if (fieldValue.length >= 2) {
                field.classList.add('is-valid');
            } else if (fieldValue.length > 0) {
                field.classList.add('is-invalid');
            }
            break;
            
        case 'idade':
            const idade = parseInt(fieldValue);
            if (idade >= 16 && idade <= 80) {
                field.classList.add('is-valid');
            } else if (fieldValue) {
                field.classList.add('is-invalid');
            }
            break;
            
        case 'numero_camisa':
            const numero = parseInt(fieldValue);
            if (numero >= 1 && numero <= 99) {
                field.classList.add('is-valid');
            } else if (fieldValue) {
                field.classList.add('is-invalid');
            }
            break;
            
        case 'ano_fundacao':
            const ano = parseInt(fieldValue);
            const anoAtual = new Date().getFullYear();
            if (ano >= 1850 && ano <= anoAtual) {
                field.classList.add('is-valid');
            } else if (fieldValue) {
                field.classList.add('is-invalid');
            }
            break;
    }
}

// Validar times diferentes em jogos
function validateDifferentTeams() {
    const timeCasa = document.querySelector('select[name="time_casa_id"]');
    const timeVisitante = document.querySelector('select[name="time_visitante_id"]');
    
    if (!timeCasa || !timeVisitante) return;
    
    const casaValue = timeCasa.value;
    const visitanteValue = timeVisitante.value;
    
    if (casaValue && visitanteValue && casaValue === visitanteValue) {
        timeVisitante.classList.add('is-invalid');
        showToast('Os times devem ser diferentes!', 'warning');
    } else {
        timeVisitante.classList.remove('is-invalid');
        if (visitanteValue && visitanteValue !== '0') {
            timeVisitante.classList.add('is-valid');
        }
    }
}

// Função para mostrar toast notifications
function showToast(message, type = 'info') {
    const toastHtml = `
        <div class="toast align-items-center text-white bg-${type} border-0 position-fixed" 
             style="top: 20px; right: 20px; z-index: 9999;" role="alert">
            <div class="d-flex">
                <div class="toast-body">${message}</div>
                <button type="button" class="btn-close btn-close-white me-2 m-auto" 
                        data-bs-dismiss="toast"></button>
            </div>
        </div>
    `;
    
    document.body.insertAdjacentHTML('beforeend', toastHtml);
    const toastElement = document.querySelector('.toast:last-child');
    const toast = new bootstrap.Toast(toastElement);
    toast.show();
    
    // Remove o elemento após ser ocultado
    toastElement.addEventListener('hidden.bs.toast', function() {
        this.remove();
    });
}

// Função para formatar data/hora no input datetime-local
function formatDateTimeLocal(date) {
    const d = new Date(date);
    const year = d.getFullYear();
    const month = String(d.getMonth() + 1).padStart(2, '0');
    const day = String(d.getDate()).padStart(2, '0');
    const hours = String(d.getHours()).padStart(2, '0');
    const minutes = String(d.getMinutes()).padStart(2, '0');
    
    return `${year}-${month}-${day}T${hours}:${minutes}`;
}

// Máscara para campos de número da camisa
document.addEventListener('DOMContentLoaded', function() {
    const numeroInputs = document.querySelectorAll('input[name="numero_camisa"]');
    numeroInputs.forEach(function(input) {
        input.addEventListener('input', function() {
            // Remove caracteres não numéricos
            this.value = this.value.replace(/[^0-9]/g, '');
            
            // Limita a 2 dígitos
            if (this.value.length > 2) {
                this.value = this.value.substr(0, 2);
            }
            
            // Valida o range
            const num = parseInt(this.value);
            if (num > 99) {
                this.value = '99';
            }
        });
    });
});

// Loading states para botões de submit
document.addEventListener('DOMContentLoaded', function() {
    const submitButtons = document.querySelectorAll('button[type="submit"]');
    submitButtons.forEach(function(button) {
        button.addEventListener('click', function(e) {
            const form = this.closest('form');
            // Adiciona estado de loading
            this.innerHTML = '<span class="spinner-border spinner-border-sm me-2"></span>Salvando...';
            this.disabled = true;
            if (form && form.checkValidity()) {
                form.submit();
            } else {
                this.innerHTML = this.getAttribute('data-original-text') || 'Salvar';
                this.disabled = false;
            }
        });
    });
});