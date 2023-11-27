package com.example.myapplication;

import android.app.Activity;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import java.util.List;
public class MemesRecicleViewAdapter extends RecyclerView.Adapter<MemeHolder>{
    private List<Memes> memes;
    private Activity activity;

    public MemesRecicleViewAdapter(List<Memes> dataSet, Activity activity) {
        this.memes=dataSet;
        this.activity=activity;
    }

    @NonNull
    @Override
    public MemeHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View gameView = LayoutInflater.from(parent.getContext()).inflate(R.layout.view_meme_cell, parent, false);
        return new MemeHolder(gameView);
    }

    @Override
    public void onBindViewHolder(@NonNull MemeHolder holder, int position) {
        Memes dataForThisCell = memes.get(position);
        holder.showData(dataForThisCell);
    }

    @Override
    public int getItemCount() { return memes.size(); }

}
