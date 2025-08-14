## Module `source/bqserver/bq/table/controllers/table_base.py`

Table base for importerters

### Classes

#### `ParseError`

#### `TableQueryLexer`

Methods:
- `t_FLOATVAL(t)`
- `t_INTVAL(t)`
- `t_STRVAL(t)`
- `t_ID(t)`
- `t_error(t)`
- `tokenize(data)`

#### `TableQueryParser`

Methods:
- `parse_filter(query, colnames)`
- `parse_agg(query, colnames)`
- `p_error(p)`
- `p_query(p)`
- `p_slice_cond(p)`
- `p_slice_list(p)`
- `p_agg_list(p)`
- `p_filter_cond(p)`
- `p_and_expr(p)`
- `p_comp_cond(p)`
- `p_unary_expr(p)`
- `p_cell_sel(p)`
- `p_single_dim_sel(p)`
- `p_range_sel(p)`
- `p_index_expr(p)`

#### `TableBase`

Formats tables into output format

Methods:
- `isloaded()`
- `close()`
- `as_array()`
- `as_table()`
- `info(**kw)`
- `run_query(query_op, sels, cond, want_cell_coord, keep_dims)`
- `read(**kw)`
- `get_queriable()`
- `get_arr()`
- `get_shape()`
- `get_columns()`
- `get_types()`
- `get_type(colname)`
- `get_slices(sels, cond)`
- `get_slice_iter(slices, cond, want_cell_coord)`
- `get_sels_iter(row_iter, sels, want_cell_coord)`
- `write(data, **kw)`
- `delete(**kw)`

#### `TableLike`

Methods:
- `get_queriable()`
- `get_slice_iter(slices, cond, want_cell_coord)`
- `get_sels_iter(row_iter, sels, want_cell_coord)`

#### `ArrayLike`

Methods:
- `get_queriable()`
- `read(**kw)`
- `get_slice_iter(slices, cond, want_cell_coord)`
- `get_sels_iter(row_iter, sels, want_cell_coord)`
