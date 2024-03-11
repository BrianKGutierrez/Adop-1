import React from "react";
import { HeaderPage } from "../../components/Admin/";
// import { TableVigilancia } from "../../components/Vigilancia/TableVigilancia";
// import { CargaVigilancia,AsignarPersonal } from "../Vigilancia";
// import { MapView } from "../../components/Vigilancia/Mapa/react-leaflet";
// import { CargaHorario } from "../../components/Vigilancia/CargaHorarios";
import { useVigilancia} from "../../hooks";
import { Button, Form } from "semantic-ui-react";
import { useFormik } from "formik";
import { Link, useLocation } from "react-router-dom";
import { ModalBasic } from "../../components/Common/ModalBasic";
import { useEffect, useState } from "react";
import Swal from "sweetalert2";
import "./HomeAdmin.scss";
// import Swal from "sweetalert2";

export function HomeAdmin() {
  const { get_vigilancia} = useVigilancia();

  const [titleModal] = useState(null);
  const [showModal, setShowModal] = useState(false);
  const [contentModal] = useState(null);
  const [refetch, setRefetch] = useState(false);
 
  useEffect(() => {
    get_vigilancia();
  }, []);

  const openCloseModal = () => {
    setShowModal((prev) => !prev);
  };
  const onRefetch = () => setRefetch((prev) => !prev);

  
  const formik = useFormik({
    // initialValues: initialValues(),
    // validationSchema: Yup.object(newSchame()),
    validateOnChange: false,
    onSubmit: async (formValue) => {
      try {
      } catch (error) {
        console.error(error);
      }
    },
  });
  return (
    <>
    <div className="transicion">
      <HeaderPage title="VIGILANCIAS" />
      <div className="header-page-vigilancia">
        <div className="formulario-buscar">
          <Form className="add-edit-user-form" onSubmit={formik.handleSubmit}>
            <div className="contenido-buscar-recargar">
              <div className="contenido-formulario-buscar">
                <div style={{ marginRight: "20px" }}>
                  
                </div>

              
              </div>

              <div></div>
            </div>
          </Form>
        </div>
       
      </div>
     
      <ModalBasic
        show={showModal}
        title={titleModal}
        children={contentModal}
        onClose={openCloseModal}
        refetch={refetch}
      />
      </div>
    </>
  );
}