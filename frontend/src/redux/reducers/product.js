import { createSlice } from "@reduxjs/toolkit";
import { getProducts } from "../actions/product";

const initialState = {
    dataProduk: [],
    isLoading: false,
    isError: false,
    errorMessage: ""
};

const productSlice = createSlice({
    name: "product",
    initialState,
    reducers: {},
    extraReducers: (builder) => {
        builder
        .addCase(getProducts.pending, (state) => {
            state.isLoading = true;
            state.isError = false;
        })
        .addCase(getProducts.fulfilled, (state, { payload }) => {
            state.dataProduk = payload;
            state.isLoading = false;
            state.isError = false;
        })
        .addCase(getProducts.rejected, (state, { payload }) => {
            state.isLoading = false;
            state.isError = true;
            state.errorMessage = payload;
        })
    }
});

export const {} = productSlice.actions;
export default productSlice.reducer;