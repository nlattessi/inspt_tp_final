function editarBorrar(claseEdit, claseDelete, modalTitle, modalForm, url, modal) {
    $(claseEdit).on('click', function(e) {
        window.location.href = $(this).data('url');
    });

    $(claseDelete).on('click', function(e) {
        document.getElementById(modalTitle).innerHTML = $(this).data('elemento');
        
        var form = document.getElementById(modalForm) || null;
        if(form) {
           form.action = url + $(this).data('id');
        }

        $(modal).modal();
    });
};

function categoriaEditarBorrar() {
    editarBorrar(
        '.catEdit',
        '.catDelete',
        'categoriaModalBorradoTitle',
        'categoriaModalBorradoForm',
        'categoria/borrar/',
        '#categoriaModalBorrado'
    );
};

function itemEditarBorrar() {
    editarBorrar(
        '.itEdit',
        '.itDelete',
        'itemModalBorradoTitle',
        'itemModalBorradoForm',
        'item/borrar/',
        '#itemModalBorrado'
    );
};