package com.example.mycatalog;

import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;

public class DetailActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        // Establece el diseño de la actividad a partir de activity_detail.xml
        setContentView(R.layout.activity_detail);
    }
}
