/** @jsx React.DOM */

var ProductRow = React.createClass({
    render: function() {
        var name = this.props.product.stocked ?
            this.props.product.name :
            <span style={{color: 'red'}}>
                {this.props.product.name}
            </span>;
        return (
            <tr>
                <td>{name}</td>
                <td>{this.props.product.price}</td>
            </tr>
        );
    }
});

var ProductTable = React.createClass({
    render: function() {
        console.log(this.props);
        var rows = [];
        this.props.products.forEach(function(product) {
            rows.push(<ProductRow product={product} key={product.name} />);
        }.bind(this));
        return (
            <table className="table table-hover">
                <thead>
                    <tr>
                        <th>Producto</th>
                        <th>Cantidad</th>
                    </tr>
                </thead>
                <tbody>{rows}</tbody>
            </table>
        );
    }
});

var SearchBar = React.createClass({
    handleChange: function() {
        this.props.onUserInput(
            this.refs.filterTextInput.getDOMNode().value,
            this.refs.inStockOnlyInput.getDOMNode().checked
        );
    },
    render: function() {
        return (
            <form>
                <input
                    type="text"
                    placeholder="Search..."
                    value={this.props.filterText}
                    ref="filterTextInput"
                    onChange={this.handleChange}
                />
                <p>
                    <input
                        type="checkbox"
                        checked={this.props.inStockOnly}
                        ref="inStockOnlyInput"
                        onChange={this.handleChange}
                    />
                    {' '}
                    Only show products in stock
                </p>
            </form>
        );
    }
});

var InputForm = React.createClass({
    handleChange: function() {
        this.props.onUserInput(
            this.refs.filterTextInput.getDOMNode().value,
            this.refs.inStockOnlyInput.getDOMNode().checked
        );
    },

    render: function() {
        return (
            <form>
                <input
                    type="number"
                    placeholder="Cantidad..."
                    value={this.props.cantNumber}
                    ref="filterTextInput"
                    onChange={this.handleChange}
                />
                <p>
                    <input
                        type="checkbox"
                        checked={this.props.inStockOnly}
                        ref="inStockOnlyInput"
                        onChange={this.handleChange}
                    />
                    {' '}
                    Pedido finalizado?
                </p>
            </form>
        );
    }
});

var COLOURS = [{
    name: "Red",
    hex: "#F21B1B"
}, {
    name: "Blue",
    hex: "#1B66F2"
}, {
    name: "Green",
    hex: "#07BA16"
}];

var SelectBox = React.createClass({
    getInitialState: function() {
        return {
            categorias: []
        };
    },

    componentDidMount: function() {
        var self = this;
        $.get(this.props.source, function(result) {
            console.log(result);
            var coleccion = result.data;
            if (this.isMounted()) {
                this.setState({
                    categorias: coleccion
                });
            }
        }.bind(this));
    },

    render: function() {
        categorias = this.state.categorias || [];
        return (
            <div>
                <select>
                {
                    categorias.map(function(categoria) {
                        return (
                            <option value={categoria.id}>{categoria.nombre}</option>
                        )
                    })
                }
                </select>
            </div>
        );
    }
});

var CategoriasCollect = React.createClass({
    getInitialState: function() {
        return {
            pCat: []
        };
    },

    componentDidMount: function() {
        var self = this;
        $.get(this.props.source, function(result) {
            var collection = result.data;
            if (this.isMounted()) {
                this.setState({
                    pCat: collection
                });
            }
        }.bind(this));
    },

    render: function() {
        images = this.state.pCat || [];
        return (
            <div>
                Cats:
                {images.map(function(image) {
                    return(
                        <ul>
                        <li>{image.id}</li>
                        <li>{image.nombre}</li>
                        <li>{image.descripcion}</li>
                        </ul>
                    )
                })}
            </div>
        );
    }
});

var FilterableProductTable = React.createClass({
    getInitialState: function() {
        return {
            cantNumber: 0,
            inStockOnly: false
        };
    },

    handleUserInput: function(cantNumber, inStockOnly) {
        // this.setState({
        //     cantNumber: cantNumber,
        //     inStockOnly: inStockOnly
        // });
    },

    render: function() {
        return (
            <div>
                <SelectBox
                    source="http://127.0.0.1:9000/jsondata/data.json"
                />
                <InputForm
                    cantNumber={this.state.cantNumber}
                    inStockOnly={this.state.inStockOnly}
                    onUserInput={this.handleUserInput}
                />
                <ProductTable
                    products={this.props.products}
                    filterText={this.state.cantNumber}
                    inStockOnly={this.state.inStockOnly}
                />
                <CategoriasCollect
                    source="http://127.0.0.1:9000/jsondata/data.json"
                />
            </div>
        );
    }
});


var PRODUCTS = [
  {category: 'Sporting Goods', price: '$49.99', stocked: true, name: 'Football'},
  {category: 'Sporting Goods', price: '$9.99', stocked: true, name: 'Baseball'},
  {category: 'Sporting Goods', price: '$29.99', stocked: false, name: 'Basketball'},
  {category: 'Electronics', price: '$99.99', stocked: true, name: 'iPod Touch'},
  {category: 'Electronics', price: '$399.99', stocked: false, name: 'iPhone 5'},
  {category: 'Electronics', price: '$199.99', stocked: true, name: 'Nexus 7'}
];

React.render(<FilterableProductTable products={PRODUCTS} />, document.getElementById("example"));