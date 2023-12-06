import {createAsyncThunk} from '@reduxjs/toolkit';
import serviceProduct from '../../services/product';

export const getProducts = createAsyncThunk("product/getProducts", async () => {
    try {
        const response = await serviceProduct.getProducts();
        console.log(response);
        return response.data;
    } catch (error) {
        return false;
    }
});