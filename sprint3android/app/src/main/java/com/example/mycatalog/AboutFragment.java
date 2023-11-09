package com.example.mycatalog;

import android.os.Bundle;
import androidx.annotation.Nullable;
import androidx.annotation.StringRes;
import androidx.fragment.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

public class AboutFragment extends Fragment {

    // Método estático para crear una nueva instancia de AboutFragment
    public static AboutFragment newInstance() {
        AboutFragment frag = new AboutFragment();
        return frag;
    }

    @Override
    public View onCreateView(LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        // Este método es llamado cuando el fragmento debe crear su vista.
        // Inflamos el diseño del fragmento (fragment_about.xml) en la vista del mismo.
        View layout = inflater.inflate(R.layout.fragment_about, container, false);
        return layout; // Devolvemos la vista inflada.
    }
}
