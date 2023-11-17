from django.contrib.auth.models import User
from django.db import models
from django.contrib import admin


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    GENDER_CHOICES = [
        ('woman', 'Woman'),
        ('man', 'Man'),
    ]
    COMPETITION_CHOICES = [
        ("ue50", "ue50"),
        ("bj", "bj"),
        ("u18", "u18"),
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='man')
    mode = models.CharField(max_length=10, choices=COMPETITION_CHOICES, default='bj')


class BJW(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    boulder_3 = models.CharField(max_length=100, default="None")
    boulder_4 = models.CharField(max_length=100, default="None")
    boulder_5 = models.CharField(max_length=100, default="None")
    boulder_6 = models.CharField(max_length=100, default="None")
    boulder_7 = models.CharField(max_length=100, default="None")
    boulder_8 = models.CharField(max_length=100, default="None")
    boulder_9 = models.CharField(max_length=100, default="None")
    boulder_10 = models.CharField(max_length=100, default="None")
    boulder_11 = models.CharField(max_length=100, default="None")
    boulder_12 = models.CharField(max_length=100, default="None")
    boulder_13 = models.CharField(max_length=100, default="None")
    boulder_14 = models.CharField(max_length=100, default="None")
    boulder_15 = models.CharField(max_length=100, default="None")
    boulder_16 = models.CharField(max_length=100, default="None")
    boulder_17 = models.CharField(max_length=100, default="None")
    boulder_18 = models.CharField(max_length=100, default="None")
    boulder_19 = models.CharField(max_length=100, default="None")
    boulder_20 = models.CharField(max_length=100, default="None")
    boulder_21 = models.CharField(max_length=100, default="None")
    boulder_22 = models.CharField(max_length=100, default="None")
    boulder_23 = models.CharField(max_length=100, default="None")
    boulder_24 = models.CharField(max_length=100, default="None")
    boulder_25 = models.CharField(max_length=100, default="None")
    boulder_26 = models.CharField(max_length=100, default="None")
    boulder_27 = models.CharField(max_length=100, default="None")
    boulder_28 = models.CharField(max_length=100, default="None")

    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    points = models.IntegerField(default=0)

    tops_amount = models.IntegerField(default=0)
    bonus_amount = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        # Calculate points based on boulder values
        self.points = self.calculate_points()
        self.tops_amount, self.bonus_amount = self.calculate_tops_and_bonuses()
        super(BJW, self).save(*args, **kwargs)

    def get_boulder_fields_and_values(self):
        # Return a dictionary of boulder field names and their values
        boulder_fields = [field.name for field in self._meta.fields if field.name.startswith("boulder_")]
        boulder_values = {field: getattr(self, field, "") for field in boulder_fields}
        return boulder_values

    def calculate_points(self):
        boulder2points_mapping = {"None": 0, "Bonus": 1, "Top": 2}

        # Calculate points for each boulder and sum them up
        points = sum(boulder2points_mapping.get(boulder, 0) for boulder in
                     [self.boulder_3, self.boulder_4, self.boulder_5, self.boulder_6, self.boulder_7, self.boulder_8,
                      self.boulder_9, self.boulder_10, self.boulder_11, self.boulder_12, self.boulder_13,
                      self.boulder_14, self.boulder_15, self.boulder_16, self.boulder_17, self.boulder_18,
                      self.boulder_19, self.boulder_20, self.boulder_21, self.boulder_22, self.boulder_23,
                      self.boulder_24, self.boulder_25, self.boulder_26, self.boulder_27, self.boulder_28])

        return points

    def calculate_tops_and_bonuses(self):
        tops = sum(1 for boulder in
                   [self.boulder_3, self.boulder_4, self.boulder_5, self.boulder_6, self.boulder_7, self.boulder_8, self.boulder_9, self.boulder_10,
                    self.boulder_11, self.boulder_12, self.boulder_13, self.boulder_14, self.boulder_15,
                    self.boulder_16, self.boulder_17, self.boulder_18, self.boulder_19, self.boulder_20,
                    self.boulder_21, self.boulder_22, self.boulder_23, self.boulder_24, self.boulder_25,
                    self.boulder_26, self.boulder_27, self.boulder_28] if
                   boulder == 'Top')
        bonuses = sum(1 for boulder in
                      [self.boulder_3, self.boulder_4, self.boulder_5, self.boulder_6, self.boulder_7, self.boulder_8, self.boulder_9, self.boulder_10,
                       self.boulder_11, self.boulder_12, self.boulder_13, self.boulder_14, self.boulder_15,
                       self.boulder_16, self.boulder_17, self.boulder_18, self.boulder_19, self.boulder_20,
                       self.boulder_21, self.boulder_22, self.boulder_23, self.boulder_24, self.boulder_25,
                       self.boulder_26, self.boulder_27, self.boulder_28] if
                      boulder == 'Bonus')
        return tops, bonuses


class BJM(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    boulder_5 = models.CharField(max_length=100, default="None")
    boulder_6 = models.CharField(max_length=100, default="None")
    boulder_7 = models.CharField(max_length=100, default="None")
    boulder_8 = models.CharField(max_length=100, default="None")
    boulder_9 = models.CharField(max_length=100, default="None")
    boulder_10 = models.CharField(max_length=100, default="None")
    boulder_11 = models.CharField(max_length=100, default="None")
    boulder_12 = models.CharField(max_length=100, default="None")
    boulder_13 = models.CharField(max_length=100, default="None")
    boulder_14 = models.CharField(max_length=100, default="None")
    boulder_15 = models.CharField(max_length=100, default="None")
    boulder_16 = models.CharField(max_length=100, default="None")
    boulder_17 = models.CharField(max_length=100, default="None")
    boulder_18 = models.CharField(max_length=100, default="None")
    boulder_19 = models.CharField(max_length=100, default="None")
    boulder_20 = models.CharField(max_length=100, default="None")
    boulder_21 = models.CharField(max_length=100, default="None")
    boulder_22 = models.CharField(max_length=100, default="None")
    boulder_23 = models.CharField(max_length=100, default="None")
    boulder_24 = models.CharField(max_length=100, default="None")
    boulder_25 = models.CharField(max_length=100, default="None")
    boulder_26 = models.CharField(max_length=100, default="None")
    boulder_27 = models.CharField(max_length=100, default="None")
    boulder_28 = models.CharField(max_length=100, default="None")
    boulder_29 = models.CharField(max_length=100, default="None")
    boulder_30 = models.CharField(max_length=100, default="None")

    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    points = models.IntegerField(default=0)
    tops_amount = models.IntegerField(default=0)
    bonus_amount = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        self.points = self.calculate_points()
        self.tops_amount, self.bonus_amount = self.calculate_tops_and_bonuses()
        super(BJM, self).save(*args, **kwargs)

    def get_boulder_fields_and_values(self):
        # Return a dictionary of boulder field names and their values
        boulder_fields = [field.name for field in self._meta.fields if field.name.startswith("boulder_")]
        boulder_values = {field: getattr(self, field, "") for field in boulder_fields}
        return boulder_values

    def calculate_points(self):
        boulder2points_mapping = {"None": 0, "Bonus": 1, "Top": 2}

        points = sum(boulder2points_mapping.get(boulder, 0) for boulder in
                     [self.boulder_5, self.boulder_6, self.boulder_7, self.boulder_8, self.boulder_9, self.boulder_10,
                      self.boulder_11, self.boulder_12, self.boulder_13, self.boulder_14, self.boulder_15,
                      self.boulder_16, self.boulder_17, self.boulder_18, self.boulder_19, self.boulder_20,
                      self.boulder_21, self.boulder_22, self.boulder_23, self.boulder_24, self.boulder_25,
                      self.boulder_26, self.boulder_27, self.boulder_28, self.boulder_29, self.boulder_30])

        return points

    def calculate_tops_and_bonuses(self):
        tops = sum(1 for boulder in
                   [self.boulder_5, self.boulder_6, self.boulder_7, self.boulder_8, self.boulder_9, self.boulder_10,
                    self.boulder_11, self.boulder_12, self.boulder_13, self.boulder_14, self.boulder_15,
                    self.boulder_16, self.boulder_17, self.boulder_18, self.boulder_19, self.boulder_20,
                    self.boulder_21, self.boulder_22, self.boulder_23, self.boulder_24, self.boulder_25,
                    self.boulder_26, self.boulder_27, self.boulder_28, self.boulder_29, self.boulder_30] if
                   boulder == 'Top')
        bonuses = sum(1 for boulder in
                      [self.boulder_5, self.boulder_6, self.boulder_7, self.boulder_8, self.boulder_9, self.boulder_10,
                       self.boulder_11, self.boulder_12, self.boulder_13, self.boulder_14, self.boulder_15,
                       self.boulder_16, self.boulder_17, self.boulder_18, self.boulder_19, self.boulder_20,
                       self.boulder_21, self.boulder_22, self.boulder_23, self.boulder_24, self.boulder_25,
                       self.boulder_26, self.boulder_27, self.boulder_28, self.boulder_29, self.boulder_30] if
                      boulder == 'Bonus')
        return tops, bonuses


class U18W(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    boulder_1 = models.CharField(max_length=100, default="None")
    boulder_2 = models.CharField(max_length=100, default="None")
    boulder_3 = models.CharField(max_length=100, default="None")
    boulder_4 = models.CharField(max_length=100, default="None")
    boulder_5 = models.CharField(max_length=100, default="None")
    boulder_6 = models.CharField(max_length=100, default="None")
    boulder_7 = models.CharField(max_length=100, default="None")
    boulder_8 = models.CharField(max_length=100, default="None")
    boulder_9 = models.CharField(max_length=100, default="None")
    boulder_10 = models.CharField(max_length=100, default="None")
    boulder_11 = models.CharField(max_length=100, default="None")
    boulder_12 = models.CharField(max_length=100, default="None")
    boulder_13 = models.CharField(max_length=100, default="None")
    boulder_14 = models.CharField(max_length=100, default="None")
    boulder_15 = models.CharField(max_length=100, default="None")
    boulder_16 = models.CharField(max_length=100, default="None")
    boulder_17 = models.CharField(max_length=100, default="None")
    boulder_18 = models.CharField(max_length=100, default="None")
    boulder_19 = models.CharField(max_length=100, default="None")
    boulder_20 = models.CharField(max_length=100, default="None")
    boulder_21 = models.CharField(max_length=100, default="None")
    boulder_22 = models.CharField(max_length=100, default="None")
    boulder_23 = models.CharField(max_length=100, default="None")
    boulder_24 = models.CharField(max_length=100, default="None")
    boulder_25 = models.CharField(max_length=100, default="None")

    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    points = models.IntegerField(default=0)
    tops_amount = models.IntegerField(default=0)
    bonus_amount = models.IntegerField(default=0)

    def save(self, *args, **kwargs):

        self.points = self.calculate_points()
        self.tops_amount, self.bonus_amount = self.calculate_tops_and_bonuses()
        super(U18W, self).save(*args, **kwargs)

    def get_boulder_fields_and_values(self):

        boulder_fields = [field.name for field in self._meta.fields if field.name.startswith("boulder_")]
        boulder_values = {field: getattr(self, field, "") for field in boulder_fields}
        return boulder_values

    def calculate_points(self):
        boulder2points_mapping = {"None": 0, "Bonus": 1, "Top": 2}

        points = sum(boulder2points_mapping.get(boulder, 0) for boulder in
                     [self.boulder_1, self.boulder_2, self.boulder_3, self.boulder_4, self.boulder_5, self.boulder_6,
                      self.boulder_7, self.boulder_8, self.boulder_9, self.boulder_10, self.boulder_11, self.boulder_12,
                      self.boulder_13, self.boulder_14, self.boulder_15, self.boulder_16, self.boulder_17,
                      self.boulder_18, self.boulder_19, self.boulder_20, self.boulder_21, self.boulder_22,
                      self.boulder_23, self.boulder_24, self.boulder_25])

        return points

    def calculate_tops_and_bonuses(self):
        tops = sum(1 for boulder in
                   [self.boulder_1, self.boulder_2, self.boulder_3, self.boulder_4, self.boulder_5, self.boulder_6,
                    self.boulder_7, self.boulder_8, self.boulder_9, self.boulder_10, self.boulder_11, self.boulder_12,
                    self.boulder_13, self.boulder_14, self.boulder_15, self.boulder_16, self.boulder_17,
                    self.boulder_18, self.boulder_19, self.boulder_20, self.boulder_21, self.boulder_22,
                    self.boulder_23, self.boulder_24, self.boulder_25] if boulder == 'Top')
        bonuses = sum(1 for boulder in
                      [self.boulder_1, self.boulder_2, self.boulder_3, self.boulder_4, self.boulder_5, self.boulder_6,
                       self.boulder_7, self.boulder_8, self.boulder_9, self.boulder_10, self.boulder_11,
                       self.boulder_12, self.boulder_13, self.boulder_14, self.boulder_15, self.boulder_16,
                       self.boulder_17, self.boulder_18, self.boulder_19, self.boulder_20, self.boulder_21,
                       self.boulder_22, self.boulder_23, self.boulder_24, self.boulder_25] if boulder == 'Bonus')
        return tops, bonuses


class U18M(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    boulder_1 = models.CharField(max_length=100, default="None")
    boulder_2 = models.CharField(max_length=100, default="None")
    boulder_3 = models.CharField(max_length=100, default="None")
    boulder_4 = models.CharField(max_length=100, default="None")
    boulder_5 = models.CharField(max_length=100, default="None")
    boulder_6 = models.CharField(max_length=100, default="None")
    boulder_7 = models.CharField(max_length=100, default="None")
    boulder_8 = models.CharField(max_length=100, default="None")
    boulder_9 = models.CharField(max_length=100, default="None")
    boulder_10 = models.CharField(max_length=100, default="None")
    boulder_11 = models.CharField(max_length=100, default="None")
    boulder_12 = models.CharField(max_length=100, default="None")
    boulder_13 = models.CharField(max_length=100, default="None")
    boulder_14 = models.CharField(max_length=100, default="None")
    boulder_15 = models.CharField(max_length=100, default="None")
    boulder_16 = models.CharField(max_length=100, default="None")
    boulder_17 = models.CharField(max_length=100, default="None")
    boulder_18 = models.CharField(max_length=100, default="None")
    boulder_19 = models.CharField(max_length=100, default="None")
    boulder_20 = models.CharField(max_length=100, default="None")
    boulder_21 = models.CharField(max_length=100, default="None")
    boulder_22 = models.CharField(max_length=100, default="None")
    boulder_23 = models.CharField(max_length=100, default="None")
    boulder_24 = models.CharField(max_length=100, default="None")
    boulder_25 = models.CharField(max_length=100, default="None")

    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    points = models.IntegerField(default=0)
    tops_amount = models.IntegerField(default=0)
    bonus_amount = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        # Calculate points based on boulder values
        self.points = self.calculate_points()
        self.tops_amount, self.bonus_amount = self.calculate_tops_and_bonuses()
        super(U18M, self).save(*args, **kwargs)

    def get_boulder_fields_and_values(self):
        # Return a dictionary of boulder field names and their values
        boulder_fields = [field.name for field in self._meta.fields if field.name.startswith("boulder_")]
        boulder_values = {field: getattr(self, field, "") for field in boulder_fields}
        return boulder_values

    def calculate_points(self):
        boulder2points_mapping = {"None": 0, "Bonus": 1, "Top": 2}

        # Calculate points for each boulder and sum them up
        points = sum(boulder2points_mapping.get(boulder, 0) for boulder in
                     [self.boulder_1, self.boulder_2, self.boulder_3, self.boulder_4, self.boulder_5, self.boulder_6,
                      self.boulder_7, self.boulder_8, self.boulder_9, self.boulder_10, self.boulder_11, self.boulder_12,
                      self.boulder_13, self.boulder_14, self.boulder_15, self.boulder_16, self.boulder_17,
                      self.boulder_18, self.boulder_19, self.boulder_20, self.boulder_21, self.boulder_22,
                      self.boulder_23, self.boulder_24, self.boulder_25])

        return points

    def calculate_tops_and_bonuses(self):
        tops = sum(1 for boulder in
                   [self.boulder_1, self.boulder_2, self.boulder_3, self.boulder_4, self.boulder_5, self.boulder_6,
                    self.boulder_7, self.boulder_8, self.boulder_9, self.boulder_10, self.boulder_11, self.boulder_12,
                    self.boulder_13, self.boulder_14, self.boulder_15, self.boulder_16, self.boulder_17,
                    self.boulder_18, self.boulder_19, self.boulder_20, self.boulder_21, self.boulder_22,
                    self.boulder_23, self.boulder_24, self.boulder_25] if boulder == 'Top')
        bonuses = sum(1 for boulder in
                      [self.boulder_1, self.boulder_2, self.boulder_3, self.boulder_4, self.boulder_5, self.boulder_6,
                       self.boulder_7, self.boulder_8, self.boulder_9, self.boulder_10, self.boulder_11,
                       self.boulder_12, self.boulder_13, self.boulder_14, self.boulder_15, self.boulder_16,
                       self.boulder_17, self.boulder_18, self.boulder_19, self.boulder_20, self.boulder_21,
                       self.boulder_22, self.boulder_23, self.boulder_24, self.boulder_25] if boulder == 'Bonus')
        return tops, bonuses


class UE50W(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    boulder_1 = models.CharField(max_length=100, default="None")
    boulder_2 = models.CharField(max_length=100, default="None")
    boulder_3 = models.CharField(max_length=100, default="None")
    boulder_4 = models.CharField(max_length=100, default="None")
    boulder_5 = models.CharField(max_length=100, default="None")
    boulder_6 = models.CharField(max_length=100, default="None")
    boulder_7 = models.CharField(max_length=100, default="None")
    boulder_8 = models.CharField(max_length=100, default="None")
    boulder_9 = models.CharField(max_length=100, default="None")
    boulder_10 = models.CharField(max_length=100, default="None")
    boulder_11 = models.CharField(max_length=100, default="None")
    boulder_12 = models.CharField(max_length=100, default="None")
    boulder_13 = models.CharField(max_length=100, default="None")
    boulder_14 = models.CharField(max_length=100, default="None")
    boulder_15 = models.CharField(max_length=100, default="None")
    boulder_16 = models.CharField(max_length=100, default="None")
    boulder_17 = models.CharField(max_length=100, default="None")
    boulder_18 = models.CharField(max_length=100, default="None")
    boulder_19 = models.CharField(max_length=100, default="None")
    boulder_20 = models.CharField(max_length=100, default="None")
    boulder_21 = models.CharField(max_length=100, default="None")
    boulder_22 = models.CharField(max_length=100, default="None")
    boulder_23 = models.CharField(max_length=100, default="None")
    boulder_24 = models.CharField(max_length=100, default="None")
    boulder_25 = models.CharField(max_length=100, default="None")

    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    points = models.IntegerField(default=0)
    tops_amount = models.IntegerField(default=0)
    bonus_amount = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        # Calculate points based on boulder values
        self.points = self.calculate_points()
        self.tops_amount, self.bonus_amount = self.calculate_tops_and_bonuses()
        super(UE50W, self).save(*args, **kwargs)

    def get_boulder_fields_and_values(self):
        # Return a dictionary of boulder field names and their values
        boulder_fields = [field.name for field in self._meta.fields if field.name.startswith("boulder_")]
        boulder_values = {field: getattr(self, field, "") for field in boulder_fields}
        return boulder_values

    def calculate_points(self):
        boulder2points_mapping = {"None": 0, "Bonus": 1, "Top": 2}

        # Calculate points for each boulder and sum them up
        points = sum(boulder2points_mapping.get(boulder, 0) for boulder in
                     [self.boulder_1, self.boulder_2, self.boulder_3, self.boulder_4, self.boulder_5, self.boulder_6,
                      self.boulder_7, self.boulder_8, self.boulder_9, self.boulder_10, self.boulder_11, self.boulder_12,
                      self.boulder_13, self.boulder_14, self.boulder_15, self.boulder_16, self.boulder_17,
                      self.boulder_18, self.boulder_19, self.boulder_20, self.boulder_21, self.boulder_22,
                      self.boulder_23, self.boulder_24, self.boulder_25])

        return points

    def calculate_tops_and_bonuses(self):
        tops = sum(1 for boulder in
                   [self.boulder_1, self.boulder_2, self.boulder_3, self.boulder_4, self.boulder_5, self.boulder_6,
                    self.boulder_7, self.boulder_8, self.boulder_9, self.boulder_10, self.boulder_11, self.boulder_12,
                    self.boulder_13, self.boulder_14, self.boulder_15, self.boulder_16, self.boulder_17,
                    self.boulder_18, self.boulder_19, self.boulder_20, self.boulder_21, self.boulder_22,
                    self.boulder_23, self.boulder_24, self.boulder_25] if boulder == 'Top')
        bonuses = sum(1 for boulder in
                      [self.boulder_1, self.boulder_2, self.boulder_3, self.boulder_4, self.boulder_5, self.boulder_6,
                       self.boulder_7, self.boulder_8, self.boulder_9, self.boulder_10, self.boulder_11,
                       self.boulder_12, self.boulder_13, self.boulder_14, self.boulder_15, self.boulder_16,
                       self.boulder_17, self.boulder_18, self.boulder_19, self.boulder_20, self.boulder_21,
                       self.boulder_22, self.boulder_23, self.boulder_24, self.boulder_25] if boulder == 'Bonus')
        return tops, bonuses


class UE50M(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    boulder_1 = models.CharField(max_length=100, default="None")
    boulder_2 = models.CharField(max_length=100, default="None")
    boulder_3 = models.CharField(max_length=100, default="None")
    boulder_4 = models.CharField(max_length=100, default="None")
    boulder_5 = models.CharField(max_length=100, default="None")
    boulder_6 = models.CharField(max_length=100, default="None")
    boulder_7 = models.CharField(max_length=100, default="None")
    boulder_8 = models.CharField(max_length=100, default="None")
    boulder_9 = models.CharField(max_length=100, default="None")
    boulder_10 = models.CharField(max_length=100, default="None")
    boulder_11 = models.CharField(max_length=100, default="None")
    boulder_12 = models.CharField(max_length=100, default="None")
    boulder_13 = models.CharField(max_length=100, default="None")
    boulder_14 = models.CharField(max_length=100, default="None")
    boulder_15 = models.CharField(max_length=100, default="None")
    boulder_16 = models.CharField(max_length=100, default="None")
    boulder_17 = models.CharField(max_length=100, default="None")
    boulder_18 = models.CharField(max_length=100, default="None")
    boulder_19 = models.CharField(max_length=100, default="None")
    boulder_20 = models.CharField(max_length=100, default="None")
    boulder_21 = models.CharField(max_length=100, default="None")
    boulder_22 = models.CharField(max_length=100, default="None")
    boulder_23 = models.CharField(max_length=100, default="None")
    boulder_24 = models.CharField(max_length=100, default="None")
    boulder_25 = models.CharField(max_length=100, default="None")

    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    points = models.IntegerField(default=0)
    tops_amount = models.IntegerField(default=0)
    bonus_amount = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        # Calculate points based on boulder values
        self.points = self.calculate_points()
        self.tops_amount, self.bonus_amount = self.calculate_tops_and_bonuses()
        super(UE50M, self).save(*args, **kwargs)

    def get_boulder_fields_and_values(self):
        # Return a dictionary of boulder field names and their values
        boulder_fields = [field.name for field in self._meta.fields if field.name.startswith("boulder_")]
        boulder_values = {field: getattr(self, field, "") for field in boulder_fields}
        return boulder_values

    def calculate_points(self):
        boulder2points_mapping = {"None": 0, "Bonus": 1, "Top": 2}

        # Calculate points for each boulder and sum them up
        points = sum(boulder2points_mapping.get(boulder, 0) for boulder in
                     [self.boulder_1, self.boulder_2, self.boulder_3, self.boulder_4, self.boulder_5, self.boulder_6,
                      self.boulder_7, self.boulder_8, self.boulder_9, self.boulder_10, self.boulder_11, self.boulder_12,
                      self.boulder_13, self.boulder_14, self.boulder_15, self.boulder_16, self.boulder_17,
                      self.boulder_18, self.boulder_19, self.boulder_20, self.boulder_21, self.boulder_22,
                      self.boulder_23, self.boulder_24, self.boulder_25])

        return points

    def calculate_tops_and_bonuses(self):
        tops = sum(1 for boulder in
                   [self.boulder_1, self.boulder_2, self.boulder_3, self.boulder_4, self.boulder_5, self.boulder_6,
                    self.boulder_7, self.boulder_8, self.boulder_9, self.boulder_10, self.boulder_11, self.boulder_12,
                    self.boulder_13, self.boulder_14, self.boulder_15, self.boulder_16, self.boulder_17,
                    self.boulder_18, self.boulder_19, self.boulder_20, self.boulder_21, self.boulder_22,
                    self.boulder_23, self.boulder_24, self.boulder_25] if boulder == 'Top')
        bonuses = sum(1 for boulder in
                      [self.boulder_1, self.boulder_2, self.boulder_3, self.boulder_4, self.boulder_5, self.boulder_6,
                       self.boulder_7, self.boulder_8, self.boulder_9, self.boulder_10, self.boulder_11,
                       self.boulder_12, self.boulder_13, self.boulder_14, self.boulder_15, self.boulder_16,
                       self.boulder_17, self.boulder_18, self.boulder_19, self.boulder_20, self.boulder_21,
                       self.boulder_22, self.boulder_23, self.boulder_24, self.boulder_25] if boulder == 'Bonus')
        return tops, bonuses


class VerificationCode(models.Model):
    code = models.CharField(max_length=10, unique=True)
    is_valid = models.BooleanField(default=True)

    def __str__(self):
        return self.code


admin.site.register(UE50W)
admin.site.register(UE50M)
admin.site.register(VerificationCode)
admin.site.register(UserProfile)
admin.site.register(BJM)
admin.site.register(BJW)
admin.site.register(U18M)
admin.site.register(U18W)
