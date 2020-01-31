import datetime

from django.urls import reverse
from rest_framework import status

from traffic_control.models import (
    BarrierPlan,
    BarrierReal,
    BarrierType,
    ConnectionType,
    Reflective,
)

from .test_base_api import TrafficControlAPIBaseTestCase


class BarrierPlanTests(TrafficControlAPIBaseTestCase):
    def test_get_all_barrier_plans(self):
        """
        Ensure we can get all barrier plan objects.
        """
        count = 3
        for i in range(count):
            self.__create_test_barrier_plan()
        response = self.client.get(reverse("api:barrierplan-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("count"), count)

    def test_get_barrier_plan_detail(self):
        """
        Ensure we can get one barrier plan object.
        """
        barrier_plan = self.__create_test_barrier_plan()
        response = self.client.get(
            reverse("api:barrierplan-detail", kwargs={"pk": barrier_plan.id})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("id"), str(barrier_plan.id))

    def test_create_barrier_plan(self):
        """
        Ensure we can create a new barrier plan object.
        """
        data = {
            "type": BarrierType.FENCE.value,
            "location": self.test_point.ewkt,
            "decision_date": "2020-01-02",
            "lifecycle": self.test_lifecycle.value,
        }
        response = self.client.post(
            reverse("api:barrierplan-list"), data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(BarrierPlan.objects.count(), 1)
        barrier_plan = BarrierPlan.objects.first()
        self.assertEqual(barrier_plan.type.value, data["type"])
        self.assertEqual(barrier_plan.location.ewkt, data["location"])
        self.assertEqual(
            barrier_plan.decision_date.strftime("%Y-%m-%d"), data["decision_date"]
        )
        self.assertEqual(barrier_plan.lifecycle.value, data["lifecycle"])

    def test_update_barrier_plan(self):
        """
        Ensure we can update existing barrier plan object.
        """
        barrier_plan = self.__create_test_barrier_plan()
        data = {
            "type": BarrierType.CONE.value,
            "location": self.test_point.ewkt,
            "decision_date": "2020-01-02",
            "lifecycle": self.test_lifecycle_2.value,
        }
        response = self.client.put(
            reverse("api:barrierplan-detail", kwargs={"pk": barrier_plan.id}),
            data,
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(BarrierPlan.objects.count(), 1)
        barrier_plan = BarrierPlan.objects.first()
        self.assertEqual(barrier_plan.type.value, data["type"])
        self.assertEqual(barrier_plan.location.ewkt, data["location"])
        self.assertEqual(
            barrier_plan.decision_date.strftime("%Y-%m-%d"), data["decision_date"]
        )
        self.assertEqual(barrier_plan.lifecycle.value, data["lifecycle"])

    def test_delete_barrier_plan_detail(self):
        """
        Ensure we can soft-delete one barrier plan object.
        """
        barrier_plan = self.__create_test_barrier_plan()
        response = self.client.delete(
            reverse("api:barrierplan-detail", kwargs={"pk": barrier_plan.id}),
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(BarrierPlan.objects.count(), 1)
        deleted_barrier_plan = BarrierPlan.objects.get(id=str(barrier_plan.id))
        self.assertEqual(deleted_barrier_plan.id, barrier_plan.id)
        self.assertEqual(deleted_barrier_plan.deleted_by, self.user)
        self.assertTrue(deleted_barrier_plan.deleted_at)

    def __create_test_barrier_plan(self):
        return BarrierPlan.objects.create(
            type=BarrierType.BOOM,
            location=self.test_point,
            decision_date=datetime.datetime.strptime("01012020", "%d%m%Y").date(),
            lifecycle=self.test_lifecycle,
            material="Betoni",
            reflective=Reflective.YES,
            connection_type=ConnectionType.OPEN_OUT,
            road_name="Testingroad",
            created_by=self.user,
            updated_by=self.user,
        )


class BarrierRealTests(TrafficControlAPIBaseTestCase):
    def test_get_all_barrier_reals(self):
        """
        Ensure we can get all real barrier objects.
        """
        count = 3
        for i in range(count):
            self.__create_test_barrier_real()
        response = self.client.get(reverse("api:barrierreal-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("count"), count)

    def test_get_barrier_real_detail(self):
        """
        Ensure we can get one real barrier object.
        """
        barrier_real = self.__create_test_barrier_real()
        response = self.client.get(
            reverse("api:barrierreal-detail", kwargs={"pk": barrier_real.id})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("id"), str(barrier_real.id))

    def test_create_barrier_real(self):
        """
        Ensure we can create a new real barrier object.
        """
        data = {
            "type": BarrierType.FENCE.value,
            "location": self.test_point.ewkt,
            "installation_date": "2020-01-02",
            "lifecycle": self.test_lifecycle.value,
        }
        response = self.client.post(
            reverse("api:barrierreal-list"), data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(BarrierReal.objects.count(), 1)
        barrier_real = BarrierReal.objects.first()
        self.assertEqual(barrier_real.type.value, data["type"])
        self.assertEqual(barrier_real.location.ewkt, data["location"])
        self.assertEqual(
            barrier_real.installation_date.strftime("%Y-%m-%d"),
            data["installation_date"],
        )
        self.assertEqual(barrier_real.lifecycle.value, data["lifecycle"])

    def test_update_barrier_real(self):
        """
        Ensure we can update existing real barrier object.
        """
        barrier_real = self.__create_test_barrier_real()
        data = {
            "type": BarrierType.CONE.value,
            "location": self.test_point.ewkt,
            "installation_date": "2020-01-21",
            "lifecycle": self.test_lifecycle_2.value,
        }
        response = self.client.put(
            reverse("api:barrierreal-detail", kwargs={"pk": barrier_real.id}),
            data,
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(BarrierReal.objects.count(), 1)
        barrier_real = BarrierReal.objects.first()
        self.assertEqual(barrier_real.type.value, data["type"])
        self.assertEqual(barrier_real.location.ewkt, data["location"])
        self.assertEqual(
            barrier_real.installation_date.strftime("%Y-%m-%d"),
            data["installation_date"],
        )
        self.assertEqual(barrier_real.lifecycle.value, data["lifecycle"])

    def test_delete_barrier_real_detail(self):
        """
        Ensure we can soft-delete one real barrier object.
        """
        barrier_real = self.__create_test_barrier_real()
        response = self.client.delete(
            reverse("api:barrierreal-detail", kwargs={"pk": barrier_real.id}),
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(BarrierPlan.objects.count(), 1)
        deleted_barrier_real = BarrierReal.objects.get(id=str(barrier_real.id))
        self.assertEqual(deleted_barrier_real.id, barrier_real.id)
        self.assertEqual(deleted_barrier_real.deleted_by, self.user)
        self.assertTrue(deleted_barrier_real.deleted_at)

    def __create_test_barrier_real(self):
        barrier_plan = BarrierPlan.objects.create(
            type=BarrierType.BOOM,
            location=self.test_point,
            decision_date=datetime.datetime.strptime("01012020", "%d%m%Y").date(),
            lifecycle=self.test_lifecycle,
            material="Betoni",
            reflective=Reflective.YES,
            connection_type=ConnectionType.OPEN_OUT,
            road_name="Testingroad",
            created_by=self.user,
            updated_by=self.user,
        )

        return BarrierReal.objects.create(
            type=BarrierType.BOOM,
            barrier_plan=barrier_plan,
            location=self.test_point,
            installation_date=datetime.datetime.strptime("20012020", "%d%m%Y").date(),
            lifecycle=self.test_lifecycle,
            material="Betoni",
            reflective=Reflective.YES,
            connection_type=ConnectionType.OPEN_OUT,
            road_name="Testingroad",
            created_by=self.user,
            updated_by=self.user,
        )
