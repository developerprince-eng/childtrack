package com.example.childtrack;


import  java.util.List;
import retrofit2.http.GET;
import retrofit2.Call;


public interface JsonPlaceHolder {

    @GET ("track")
    Call<List<Location>> getLocations();
}
